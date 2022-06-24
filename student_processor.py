from Student import Student 

def load_students():
    try:
        file = open("students2.csv", "r")
        counter = 0
        student_data = []
        for line in file:
            counter += 1
            if counter == 1:
                continue
            individual_data = line.split(",")
            if len(individual_data) != 6:
                raise Exception(f"There is an error in your file on line {counter}.")
            first_name = individual_data[0]
            last_name = individual_data[1]
            major = individual_data[2]
            credit_hours = individual_data[3]
            gpa = individual_data[4]
            student_id = individual_data[5]
            stud = Student(first_name, last_name, major, credit_hours, gpa, student_id)
            student_data.append(stud)

    except Exception as err:
        print(err)
    finally:
        file.close()
    return student_data

def sort_list(list_of_students):
    list_of_students.sort(key=lambda the_student: the_student.get_major())
    return list_of_students

def print_student_data(list_of_students):
    for student in list_of_students:
        print(f"{student.get_first_name()} {student.get_last_name()}: {student.get_major()}")
        print(f"GPA: {student.get_gpa()}")
        print(f"Class: {student.get_class_level()}")
        print(f"ID: {student.get_student_id()}\n")
    return

    
def main():
    list_of_students = load_students()
    list_of_students = sort_list(list_of_students)
    print_student_data(list_of_students)

main()