
def validate_input(prompt, data_type):
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid value.")