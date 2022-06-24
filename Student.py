
class Student:
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_major(self):
        return self.__major

    def get_credit_hours(self):
        return self.__credit_hours

    def get_gpa(self):
        return self.__gpa

    def get_student_id(self):
        return self.__student_id

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_major(self, new_major):
        self.__major = new_major

    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def update_credit_hours(self, new_credits):
        self.__credit_hours += new_credits

    def get_class_level(self):
        if float(self.__credit_hours) >= 90:
            return "Senior"
        elif float(self.__credit_hours) >= 60:
            return "Junior"
        elif float(self.__credit_hours) >= 30:
            return "Sophomore"
        else:
            return "Freshman"
