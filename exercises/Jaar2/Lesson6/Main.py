from Jaar2.Lesson6.Student import Student
from Jaar2.Lesson6.Class import Class

stu1 = Student('01', 'tst1', 2, 'tst@tsr.nl', '1-1-1990')
stu2 = Student('02', 'tst2', 2, 'tst@tsr.nl', '1-1-1990')
stu3 = Student('03', 'tst3', 2, 'tst@tsr.nl', '1-1-1990')
stu4 = Student('04', 'tst4', 2, 'tst@tsr.nl', '1-1-1990')

students = [stu1, stu2, stu3, stu4]

cl = Class('APM2', students)

print(cl.get_students())

cl.create_student()

print(cl.get_students())

for student in cl.get_students():
    print(student.get_name())


