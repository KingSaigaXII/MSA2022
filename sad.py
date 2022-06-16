from itertools import count


print ("Welcome to the SAD (Student/Administrator Database).")
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
    f = open("accountdata.txt", "r")
    input_username = input("Please enter your username.")
    input_password = input("Please enter your password.")
    if input_username 
