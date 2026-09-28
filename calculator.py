# calculator.py
# Handles basic arithmetic calculations


def parse_expression(expression):
    parts = expression.split()

    if len(parts) != 3:
        raise ValueError("Please use the format: number operator number")

    first_number = float(parts[0])
    operator = parts[1]
    second_number = float(parts[2])

    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operator. Use +, -, *, or /.")

    return first_number, operator, second_number


def calculate(first_number, operator, second_number):

    if operator == "+":
        return first_number + second_number

    elif operator == "-":
        return first_number - second_number

    elif operator == "*":
        return first_number * second_number

    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first_number / second_number