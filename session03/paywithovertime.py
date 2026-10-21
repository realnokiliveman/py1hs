hours = input("Enter Hours: ")
if  hours != "" and not hours.isdigit():
    print("Invalid input. Please enter a valid number of hours (0-168).")
    exit()
hours = int(hours)
if hours < 0 or hours > 168:
    print("Invalid input. Please enter a valid number of hours (0-168).")
    exit()

rate = float(input("Enter Rate: "))

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    regular_pay = 40 * rate
    total_pay = regular_pay + overtime_pay
    print(f"Total pay: {total_pay:.2f}")
else:
    total_pay = hours * rate
    print(f"Total pay: {total_pay:.2f}")