from helper import validate_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_units = user_input.split(':')
    print(days_and_units)

    days_and_units_dict = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dict)

    validate_execute(days_and_units_dict)
