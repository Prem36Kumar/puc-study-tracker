def calculate_average_marks(marks_records):
    """
    marks_records: list of tuples from database (id, subject_id, mark)
    """
    if not marks_records:
        return 0

    total = sum(record[2] for record in marks_records)
    return total / len(marks_records)


def calculate_attendance_percentage(attendance_records):
    """
    attendance_records: list of tuples (id, subject_id, attended, total)
    """
    if not attendance_records:
        return 0

    attended_sum = sum(record[2] for record in attendance_records)
    total_sum = sum(record[3] for record in attendance_records)

    if total_sum == 0:
        return 0

    return (attended_sum / total_sum) * 100


def calculate_grade(average_marks):
    """
    Returns performance grade based on marks
    """
    if average_marks >= 90:
        return "A"
    elif average_marks >= 75:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    else:
        return "F"
