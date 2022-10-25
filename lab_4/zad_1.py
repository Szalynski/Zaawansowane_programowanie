class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student o imieniu {self.name}'

    def is_passed(self) -> bool:
        avg = sum(self.marks) / len(self.marks)
        return True if avg > 50 else False
