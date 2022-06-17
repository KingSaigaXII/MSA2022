from itertools import count



print("Welcome to the SAD (Student/Administrator Database).")
choice = float(input("Please either create an account (1) or log in to an existing account (2): "))
if choice == 1:
    username = input("Please enter a username: ")
    while len(username) < 4 or len(username) > 16:      
        if len(username) < 4:
            username = input("Username is too short! Please enter a username longer than 3 characters: ")
        if len(username) > 16:
            username = input("Username is too long! Please enter a username shorter than 17 characters: ")
    password = input("Please enter a password: ")
    while len(password) < 6 or len(password) > 12:
        if len(password) < 6:
            password = input("Password is too short! Please enter a password longer than 5 characters: ")
        if len(password) > 12:
            password = input("Password is too long! Please enter a password shorter than 13 characters: ")
    f = open("accountdata.txt", "a")
    f.write(f"{username}, {password}\n")
    f.close()
    print("Account successfully created.")
if choice == 2:
    file = open("accountdata.txt", "r")
    logged_in = False
    while (True):
        input_username = input("Please enter a valid username: ")
        input_password = input("Please enter a valid password: ")
        for line in file:
            correct_data = line.split(", ")
            #compare username to correctData[0] and pass to correctData[1]
            if input_username == correct_data[0] and input_password == correct_data[1].strip("\n"):
                logged_in  = True
                break
            #if there is a match. move on
            #if not match do again
        if logged_in == True:
            break
print("Login successful!")
if logged_in==True:
    input_grade="Yes"
    gradeNumber=0
    grades=[]
    while input_grade=="Yes":
        gradeNumber+=1
        studentName=input("What is the name of the student? ")
        studentGrade=float(input("What is the student's number grade? "))
        if studentGrade>=90:
            studentLetter="A"
        elif studentGrade<90 and studentGrade>=80:
            studentLetter="B"
        elif studentGrade<80 and studentGrade>=70:
            studentLetter="C"
        elif studentGrade<70 and studentGrade>=60:
            studentLetter="D"
        elif studentGrade<60:
            studentLetter="F"
        print()
        print(f"Student name: {studentName}")
        print(f"Student grade: {studentGrade}, {studentLetter}")
        print()
        grades.append(studentGrade)
        input_grade=input("Do you want to input another grade? (Yes/No) ")

    calc=input("Calculate average? (Y/N) ")
    if calc == "Y":
        average=0
        for number in grades:
            average=average+number
        average=average//gradeNumber
        print(f"The average grade is: {average}")
else:
    pass
                
            
   

        
       