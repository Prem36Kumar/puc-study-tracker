import sqlite3

DB_NAME = "project.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    with connect() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            mark INTEGER,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            attended INTEGER,
            total INTEGER,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
        """)


# -------------------------
# Subject Functions
# -------------------------

def add_subject(name):
    with connect() as conn:
        cursor = conn.cursor()

        # Check if subject already exists
        cursor.execute("SELECT * FROM subjects WHERE name = ?", (name,))
        existing = cursor.fetchone()

        if existing:
            print("Subject already exists!")
            return

        cursor.execute("INSERT INTO subjects (name) VALUES (?)", (name,))
        print("Subject added successfully!")


def get_all_subjects():
    with connect() as conn:
        return conn.execute("SELECT * FROM subjects").fetchall()


# -------------------------
# Marks Functions
# -------------------------

def add_mark(subject_id, mark):
    with connect() as conn:
        conn.execute(
            "INSERT INTO marks (subject_id, mark) VALUES (?, ?)",
            (subject_id, mark)
        )


def get_marks_by_subject(subject_id):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM marks WHERE subject_id=?",
            (subject_id,)
        ).fetchall()


# -------------------------
# Attendance Functions
# -------------------------

def add_attendance(subject_id, attended, total):
    with connect() as conn:
        conn.execute(
            "INSERT INTO attendance (subject_id, attended, total) VALUES (?, ?, ?)",
            (subject_id, attended, total)
        )


def get_attendance_by_subject(subject_id):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM attendance WHERE subject_id=?",
            (subject_id,)
        ).fetchall()
