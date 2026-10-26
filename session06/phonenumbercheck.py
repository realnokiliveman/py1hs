p_num = input("Enter a phone number: ")

def clean_number(text):
    
    cleaned = text.strip()
    cleaned = cleaned.replace(" ", "")
    return cleaned

def is_valid(number):
    if len(number) == 10 and number[0] == "0" and number.isdigit():
        return True
    else:
        return False


def format_number(number):
    return f"{number[:3]}-{number[3:6]}-{number[6:]}" 

def hide_number(number):
    return f"{number[:3]}-***-{number[-4:]}"

def sum_digits(number):
    return sum(int(digit) for digit in number if digit.isdigit())

def main():
    cleaned_number = clean_number(p_num)
    if is_valid(cleaned_number):
        formatted = format_number(cleaned_number)
        hidden = hide_number(cleaned_number)
        digit_sum = sum_digits(cleaned_number)
        print(f"Formatted number: {formatted}")
        print(f"Hidden number: {hidden}")
        print(f"Sum of digits: {digit_sum}")
    else:
        print("Invalid phone number.")

if __name__ == "__main__":
    main()