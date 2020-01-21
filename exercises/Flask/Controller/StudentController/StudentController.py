from flask import Blueprint
from Model.Student import Student
import jsonpickle

student_controller = Blueprint('student_controller', __name__)

stu1 = Student('01', 'tst1', 2, 'tst@tsr.nl', '1-1-1990')
stu2 = Student('02', 'tst2', 2, 'tst@tsr.nl', '1-1-1990')
stu3 = Student('03', 'tst3', 2, 'tst@tsr.nl', '1-1-1990')
stu4 = Student('04', 'tst4', 2, 'tst@tsr.nl', '1-1-1990')

students = [stu1, stu2, stu3, stu4]


@student_controller.route('/student')
def get_students():
    return jsonpickle.encode({'students': students}, unpicklable=False)


@student_controller.route('/student/add', methods=['POST'])
def add_student():
    students.append(Student('05', 'dfdsf', 3, 'sdffds', 'sdfds'))

    return get_students()
