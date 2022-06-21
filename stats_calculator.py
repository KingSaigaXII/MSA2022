from operator import index
import os.path

def get_file_name():
    while True:
        user_input = input("Enter file name: ")
        if user_input == "":
            print("ERROR: Please enter a value.\n")
            continue
        elif not os.path.exists(user_input):
            print("ERROR: File does not exist.\n")
            continue
        else:
            break
    return user_input

def load_numbers_list(file_name):
    file = open(file_name, "r")
    numbers_list = []
    for number in file:
        numbers_list.append(int(number))
    return numbers_list

def calculate_median(list_of_numbers):
    list_of_numbers.sort()
    if (len(list_of_numbers) % 2 == 0):
        is_even = True
    else:
        is_even = False
    if is_even:
        index_1 = int(len(list_of_numbers) / 2)
        index_2 = index_1 -1
        median = (list_of_numbers [index_1] + list_of_numbers[index_2]) / 2
    else:
        median = list_of_numbers[index]
        index = int((len(list_of_numbers) - 1) / 2)
    return median

def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    list_of_numbers = load_numbers_list(file_name)
    if len(list_of_numbers) == 0:
        print("File was empty.")
    elif len(list_of_numbers) == 1:
        print("Only one number in file.")
    else:  
        median = calculate_median(list_of_numbers)
        print(median)
    #load numbers from file into a list
    
main()
