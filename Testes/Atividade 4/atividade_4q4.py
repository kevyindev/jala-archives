class ClassRoom:
    def __init__(self):
        self.students = ["Maria", "George", "Pablo", "Lucas", "Marco", "Tony", "Diego"]

    def check_student(self, student):
        return student.lower() in [s.lower() for s in self.students]

classroom = ClassRoom()
print(classroom.check_student("Maria"))
print(classroom.check_student("maria"))
print(classroom.check_student("João"))