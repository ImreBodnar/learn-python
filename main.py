# variables
calc_to_units = 24
unit_name = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_units} {unit_name}."


def validate_execute():
    if user_input.isdigit():
        user_value = int(user_input)
        if user_value > 0:
            calculated_value = days_to_units(user_value)
            print(f"Calculated value: {calculated_value}")
        elif user_value == 0:
            print("it's zero")
    else:
        print("Input is not digit!")


user_input = input("Enter a number of days: ")
print(f"Given value: {user_input}")

validate_execute()
