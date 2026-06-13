def days_to_units(num_of_days, unit):
    if unit == "hour":
        return f"{num_of_days} days are {num_of_days * 24} hours."
    elif unit == "minute":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes."
    else:
        return "Unsupported unit!"


def validate_execute(input_dict):
    try:
        user_value = int(input_dict["days"])
        if user_value > 0:
            calculated_value = days_to_units(user_value, input_dict["unit"])
            print(f"Calculated value: {calculated_value}")
        elif user_value == 0:
            print("It's zero")
        else:
            print("It's negative")
    except ValueError:
        print("It's not digit!")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days and a unit: ")
    days_and_units = user_input.split(':')
    print(days_and_units)

    days_and_units_dict = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dict)

    validate_execute(days_and_units_dict)
