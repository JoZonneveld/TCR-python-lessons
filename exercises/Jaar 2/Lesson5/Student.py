class Student:
    def __init__(self, student_nr, name, year, email, birthday):
        self.student_nr = student_nr
        self.name = name
        self.year = year
        self.email = email
        self.birthday = birthday

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

