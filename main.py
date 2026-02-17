import tkinter as tk
from tkinter import messagebox
from database import DatabaseManager

db = DatabaseManager()

class StudyTrackerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PUC Study Tracker")
        self.root.geometry("500x500")
        self.current_user = None
        self.login_screen()

    def login_screen(self):
        self.clear()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if db.register_user(username, password):
            messagebox.showinfo("Success", "User Registered")
        else:
            messagebox.showerror("Error", "Username already exists")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_id = db.login_user(username, password)

        if user_id:
            self.current_user = user_id
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def dashboard(self):
        self.clear()

        tk.Label(self.root, text="Dashboard", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Add Study Session",
                  command=self.add_session_screen).pack(pady=5)

        tk.Button(self.root, text="View Streak",
                  command=self.show_streak).pack(pady=5)

        tk.Button(self.root, text="Logout",
                  command=self.login_screen).pack(pady=5)

    def add_session_screen(self):
        self.clear()

        tk.Label(self.root, text="Add Study Session").pack(pady=5)

        self.subject_var = tk.StringVar(value="Physics")

        tk.OptionMenu(self.root, self.subject_var,
                      "Physics", "Math", "Computer Science").pack(pady=5)

        self.hours_entry = tk.Entry(self.root)
        self.hours_entry.insert(0, "Hours")
        self.hours_entry.pack(pady=5)

        self.diff_entry = tk.Entry(self.root)
        self.diff_entry.insert(0, "Difficulty (1-10)")
        self.diff_entry.pack(pady=5)

        self.mood_entry = tk.Entry(self.root)
        self.mood_entry.insert(0, "Mood")
        self.mood_entry.pack(pady=5)

        self.notes_entry = tk.Entry(self.root)
        self.notes_entry.insert(0, "Notes")
        self.notes_entry.pack(pady=5)

        tk.Button(self.root, text="Save",
                  command=self.save_session).pack(pady=5)

        tk.Button(self.root, text="Back",
                  command=self.dashboard).pack(pady=5)

    def save_session(self):
        try:
            hours = float(self.hours_entry.get())
            difficulty = int(self.diff_entry.get())

            if difficulty < 1 or difficulty > 10:
                raise ValueError

            db.add_session(
                self.current_user,
                self.subject_var.get(),
                hours,
                difficulty,
                self.mood_entry.get(),
                self.notes_entry.get()
            )

            messagebox.showinfo("Success", "Session Saved")
            self.dashboard()

        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def show_streak(self):
        streak = db.calculate_streak(self.current_user)
        messagebox.showinfo("Study Streak", f"Current Streak: {streak} days")

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTrackerApp(root)
    root.mainloop()


