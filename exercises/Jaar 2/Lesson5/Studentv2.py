class Student:
    def __init__(self, student_nr, name, year, email, birthday):
        self.__student_nr = student_nr
        self.__name = name
        self.__year = year
        self.__email = email
        self.__birthday = birthday

    def get_student_nr(self):
        return self.__student_nr

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_year(self):
        return self.__year


stu1 = Student('01', 'tst1', 1, 'tst@tsr.nl', '1-1-1990')
stu2 = Student('02', 'tst2', 2, 'tst@tsr.nl', '1-1-1990')
stu3 = Student('03', 'tst3', 3, 'tst@tsr.nl', '1-1-1990')
stu4 = Student('04', 'tst4', 3, 'tst@tsr.nl', '1-1-1990')

students = [stu1, stu2, stu3, stu4]

for student in filter(lambda x: x.get_year() == 3, students):
    print(student.get_name())

# Map example
'''
for student_nr in map(lambda x: x.get_student_nr(), students):
    print(student_nr)
'''

# Filter example

for student in filter(lambda x: x.get_year() == 3, students):
    print(student.get_name())
