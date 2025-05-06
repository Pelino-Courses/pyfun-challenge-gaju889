from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name, email, student_id, department):
        Student.__init__(self, name, email, student_id)
        Instructor.__init__(self, name, email, department)
