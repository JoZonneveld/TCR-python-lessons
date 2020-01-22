from flask import Blueprint, request
from Flask.Model.Student import Student
import jsonpickle

student_controller = Blueprint('student_controller', __name__)

stu1 = Student('01', 'tst1', 2, 'tst@tsr.nl', '1-1-1990')
stu2 = Student('02', 'tst2', 2, 'tst@tsr.nl', '1-1-1990')
stu3 = Student('03', 'tst3', 2, 'tst@tsr.nl', '1-1-1990')
stu4 = Student('04', 'tst4', 2, 'tst@tsr.nl', '1-1-1990')

students = [stu1, stu2, stu3, stu4]


@student_controller.route('/student')
def get_students():
    return jsonpickle.encode(students, unpicklable=False)


@student_controller.route('/student/add', methods=['POST'])
def add_student():
    if request.method == 'POST':
        student_nr = request.json['student_nr']
        name = request.json['name']
        year = request.json['year']
        email = request.json['email']
        birthday = request.json['birthday']

        print(request.json)
        new_student = Student(student_nr, name, year, email, birthday)
        students.append(new_student)
        return jsonpickle.encode({new_student}, unpicklable=False)
