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
