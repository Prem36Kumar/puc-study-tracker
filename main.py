from database import (
    create_tables,
    add_subject,
    add_mark,
    add_attendance,
    get_all_subjects,
    get_marks_by_subject,
    get_attendance_by_subject
)


def clear_line():
    print("-" * 40)


def main():
    create_tables()

    while True:
        clear_line()
        print("📘 PUC STUDY TRACKER")
        clear_line()
        print("1. Add Subject")
        print("2. Add Marks")
        print("3. Add Attendance")
        print("4. View Subjects")
        print("5. View Subject Report")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_subject_menu()
        elif choice == "2":
            add_marks_menu()
        elif choice == "3":
            add_attendance_menu()
        elif choice == "4":
            view_subjects_menu()
        elif choice == "5":
            subject_report_menu()
        elif choice == "6":
            print("\nThank you for using PUC Study Tracker 👋")
            break
        else:
            print("Invalid choice. Please try again.")


# ---------------- MENU FUNCTIONS ---------------- #

def add_subject_menu():
    clear_line()
    name = input("Enter subject name: ").strip()

    if not name:
        print("Subject name cannot be empty.")
        return

    add_subject(name)
    print("Subject added successfully!")


def add_marks_menu():
    clear_line()
    subject_id = input("Enter subject ID: ").strip()
    mark = input("Enter marks: ").strip()

    if not subject_id.isdigit() or not mark.isdigit():
        print("Please enter valid numeric values.")
        return

    add_mark(int(subject_id), int(mark))
    print("Marks added successfully!")


def add_attendance_menu():
    clear_line()
    subject_id = input("Enter subject ID: ").strip()
    attended = input("Classes attended: ").strip()
    total = input("Total classes: ").strip()

    if not (subject_id.isdigit() and attended.isdigit() and total.isdigit()):
        print("Please enter valid numeric values.")
        return

    add_attendance(int(subject_id), int(attended), int(total))
    print("Attendance recorded successfully!")


def view_subjects_menu():
    clear_line()
    subjects = get_all_subjects()

    if not subjects:
        print("No subjects found.")
        return

    print("📚 Subjects List")
    clear_line()
    for subject in subjects:
        print(f"ID: {subject[0]} | Name: {subject[1]}")


def subject_report_menu():
    clear_line()
    subject_id = input("Enter subject ID: ").strip()

    if not subject_id.isdigit():
        print("Invalid subject ID.")
        return

    subject_id = int(subject_id)

    marks = get_marks_by_subject(subject_id)
    attendance = get_attendance_by_subject(subject_id)

    clear_line()
    print("📊 Subject Report")
    clear_line()

    # Marks Report
    if marks:
        average = sum(m[2] for m in marks) / len(marks)
        print(f"Average Marks: {average:.2f}")
    else:
        print("No marks recorded.")

    # Attendance Report
    if attendance:
        attended = sum(a[2] for a in attendance)
        total = sum(a[3] for a in attendance)

        if total > 0:
            percentage = (attended / total) * 100
            print(f"Attendance: {percentage:.2f}%")
        else:
            print("No attendance data.")
    else:
        print("No attendance recorded.")


if __name__ == "__main__":
    main()
