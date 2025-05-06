from person import Person

class Instructor(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department
