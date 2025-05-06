from teaching_assistant import TeachingAssistant

if __name__ == "__main__":
    ta = TeachingAssistant("Alex", "alex@example.com", "S123", "Computer Science")
    print(f"{ta.name} - Student ID: {ta.student_id} - Dept: {ta.department}")
