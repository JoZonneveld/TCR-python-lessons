import random as rnd
from Jaar2.Lesson6.Student import Student


class Class:
    def __init__(self, name, students=None):
        self.__name = name
        self.__students = [] if students is None else students

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def create_student(self):
        student_nr = rnd.randint(0, 9999999)
        name = input('Wat is de naam van de student? ')
        year = int(input('Welk jaar zit de student? '))
        email = input('Wat is het email adres van de student? ')
        birthday = input('Wat is de geboorte datum van de student? ')

        new_student = Student(student_nr, name, year, email, birthday)

        self.add_student(new_student)
