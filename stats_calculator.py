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
        index = int((len(list_of_numbers) - 1) / 2)
        median = list_of_numbers[index] 
    return median

def determine_mode(list_of_numbers):
    modal_values = {}
    list_of_modal_values = []
    for number in list_of_numbers:
        if number in modal_values:
            modal_values[number] += 1
        else:
            modal_values[number] = 1
    list_values = modal_values.values()
    max_value = max(list_values)
    for key in modal_values:
        if modal_values[key] == max_value:
            list_of_modal_values.append(key)
    return list_of_modal_values
    
def determine_maximum(list_of_numbers):
    maximum = list_of_numbers[1]
    for number in list_of_numbers:
        if number > maximum:
            maximum = number
    return maximum

def determine_minimum(list_of_numbers):
    minimum = list_of_numbers[1]
    for number in list_of_numbers:
        if number < minimum:
            minimum = number
    return minimum

def determine_sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum

def prompt_rerun():
    user_input = input("Would you like to run this program for another file? (Y/N) ")
    if user_input == "Y":
        main()
    elif user_input == "N":
        print("Adios")
    else:
        print("Incorrect input. Please try again. \n")
        prompt_rerun()

def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    list_of_numbers = load_numbers_list(file_name)
    if len(list_of_numbers) == 0:
        print("File was empty.")
    elif len(list_of_numbers) == 1:
        print("Only one number in file.")
    else:  
        maximum = determine_maximum(list_of_numbers)
        minimum = determine_minimum(list_of_numbers)
        sum = determine_sum(list_of_numbers)
        count = len(list_of_numbers)
        average = round(sum / count, 3)
        range = maximum - minimum
        median = calculate_median(list_of_numbers)
        list_of_modal_values = determine_mode(list_of_numbers)
        print(f"File Name: {file_name}")
        print(f"Sum: {sum}")
        print(f"Count: {count}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
        print(f"Range: {range}")
        print(f"Median: {median}")
        print(f"Mode: {list_of_modal_values}")
        prompt_rerun()
    
main()
