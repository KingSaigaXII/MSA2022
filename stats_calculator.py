def get_file_name():
    user_input = input("Enter file name: ")
    try:
        open(user_input)
    except:
        print("Incorrect input type. Please enter a valid file name.")
        get_file_name()
    else:
        return user_input

def load_numbers_list(file_name):
    file = open(file_name, "r")
    numbers_list = []
    for line in file:
        numbers_list.append(int(line))
    return numbers_list

def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    list_of_numbers = load_numbers_list(file_name)
    print(list_of_numbers)
    #load numbers from file into a list
    
main()