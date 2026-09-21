import json

def load_attendance():
    with open("attendance_log.json", "r") as file:
        return json.load(file)

    def calculate_attendance(student_id, records):
    student_records = [
        record for record in records
        if record["student_id"] == student_id
    ]

    total_days = len(student_records)

    if total_days == 0:
        return 0

    present_days = sum(
        1 for record in student_records
        if record["status"] == "Present"
    )

    return (present_days / total_days) * 100

def chronic_absentees(records):
    students = {}

    for record in records:
        student_id = record["student_id"]
        name = record["name"]

        if student_id not in students:
            students[student_id] = name

    results = []

    for student_id, name in students.items():
        rate = calculate_attendance(student_id, records)

        if rate < 85:
            results.append({
                "student_id": student_id,
                "name": name,
                "attendance_rate": rate
            })

    return results

def display_chronic_absentees():
    records = load_attendance()

    students = chronic_absentees(records)

    print("\n--- Chronic Absentee Report ---")

    if not students:
        print("No students are below 85% attendance.")
        return

    for student in students:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['attendance_rate']:.2f}%"
        )

def display_chronic_absentees():
    records = load_attendance()

    students = chronic_absentees(records)

    print("\n--- Chronic Absentee Report ---")

    if not students:
        print("No students are below 85% attendance.")
        return

    for student in students:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['attendance_rate']:.2f}%"
        )

def longest_absence_streak(student_id, records):
    student_records = [
        record for record in records
        if record["student_id"] == student_id
    ]

    current_streak = 0
    longest_streak = 0

    for record in student_records:
        if record["status"] == "Absent":
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    return longest_streak
