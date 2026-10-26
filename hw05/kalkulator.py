def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None


def main():
    while True:
        first = input("First number (or q): ")
        if first == "q":
            break
        a = float(first)
        operator = input("Operator (+ - * /): ")
        b = float(input("Second number: "))
        result = calculate(a, operator, b)
        if result is None:
            print("Cannot calculate that")
        else:
            print("Result:", result)


if __name__ == "__main__":
    main()