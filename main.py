# variables
calc_to_units = 24
unit_name = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_units} {unit_name}."


def validate_execute():
    try:
        user_value = int(user_input)
        if user_value > 0:
            calculated_value = days_to_units(user_value)
            print(f"Calculated value: {calculated_value}")
        elif user_value == 0:
            print("It's zero")
        else:
            print("It's negative")
    except ValueError:
        print("It's not digit!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days: ")
    print(f"Given value: {user_input}")
    validate_execute()
