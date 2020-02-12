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
        student_nr = input('Vul een studentnr in: ')
        name = input('Vul een naam in: ')
        year = int(input('voer een jaar in: '))
        email = input('Vul een email in: ')
        birthday = input('Vul een birthday in: ')

        new_student = Student(student_nr, name, year, email, birthday)
        self.add_student(new_student)
        print(new_student)
