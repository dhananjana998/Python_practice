class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks! Enter between 0 and 100")

student1 = Student("Sachini", 80)
print(student1.marks)
student1.marks = 95
print(student1.marks)
student1.marks = 120   
