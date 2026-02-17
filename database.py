import sqlite3
import bcrypt
from datetime import datetime, timedelta

DB_NAME = "study_tracker.db"

class DatabaseManager:
    def set_weekly_goal(self, user_id, target_hours):
        self.cursor.execute("""
        INSERT INTO goals (user_id, weekly_target)
        VALUES (?, ?)
        """, (user_id, target_hours))
        self.conn.commit()

    def get_weekly_goal(self, user_id):
        self.cursor.execute("""
        SELECT weekly_target FROM goals
        WHERE user_id=?
        ORDER BY id DESC LIMIT 1
        """, (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password BLOB NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT,
            hours REAL,
            difficulty INTEGER,
            mood TEXT,
            notes TEXT,
            date TEXT
        )
        """)

        self.conn.commit()

    def register_user(self, username, password):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login_user(self, username, password):
        self.cursor.execute(
            "SELECT id, password FROM users WHERE username=?",
            (username,)
        )
        result = self.cursor.fetchone()

        if result:
            user_id, stored_hash = result
            if bcrypt.checkpw(password.encode(), stored_hash):
                return user_id
        return None

    def add_session(self, user_id, subject, hours, difficulty, mood, notes):
        date_now = datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute("""
        INSERT INTO study_sessions
        (user_id, subject, hours, difficulty, mood, notes, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, subject, hours, difficulty, mood, notes, date_now))

        self.conn.commit()

    def calculate_streak(self, user_id):
        self.cursor.execute("""
        SELECT DISTINCT date FROM study_sessions
        WHERE user_id=?
        ORDER BY date DESC
        """, (user_id,))

        dates = [row[0] for row in self.cursor.fetchall()]

        if not dates:
            return 0

        streak = 1
        previous = datetime.strptime(dates[0], "%Y-%m-%d")

        for d in dates[1:]:
            current = datetime.strptime(d, "%Y-%m-%d")
            if previous - current == timedelta(days=1):
                streak += 1
                previous = current
            else:
                break

        return streak
