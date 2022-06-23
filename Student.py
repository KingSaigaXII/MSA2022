
class Student:
    def __init__(self, first_name, last_name, major, gpa, class_level, id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__gpa = gpa
        self.__class_level = class_level
        self.__id = id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_major(self):
        return self.__major

    def get_gpa(self):
        return self.__gpa

    def get_class_level(self):
        return self.__class_level

    def get_id(self):
        return self.__id

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_major(self, new_major):
        self.__major = new_major

    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def set_class_level(self, new_class_level):
        self.__class_level = new_class_level

stud = Student("Yrwin", "Batan", "Chemistry", "4.5", "Junior", "12412310")
