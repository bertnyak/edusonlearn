class Student:
    def __init__(self, name, age, major, gpa=0):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Специальность: {self.major}, Средний балл: {self.gpa}"

    def strip_code(self):
        self.name = ''.join(filter(lambda x: x.isalpha(), self.name))


class GraduateStudent(Student):
    def __init__(self, name, age, major, gpa, education_level):
        super().__init__(name, age, major, gpa)
        self.education_level = education_level

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Специальность: {self.major}, Средний балл: {self.gpa}, Уровень образования: {self.education_level}"

    def strip_code(self):
        self.name = ''.join(filter(lambda x: x.isalpha(), self.name))


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Предмет: {self.subject}"

    def strip_code(self):
        self.name = ''.join(filter(lambda x: x.isalpha(), self.name))


class University:
    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers

    def get_info(self):
        return f"Название: {self.name}, Студенты: {self.students}, Учителя: {self.teachers}"


a = Student('Tom Smith', 21, 'Computer Science', 4.5)
print(a.get_info())
print(a.strip_code())
print(a.get_info())

b = GraduateStudent('John Doe', 22, 'Computer Science', 4.5, 'Master')
print(b.get_info())
print(b.strip_code())
print(b.get_info())

c = Teacher('Oliver Smith', 30, 'Computer Science')
print(c.get_info())
print(c.strip_code())
print(c.get_info())
