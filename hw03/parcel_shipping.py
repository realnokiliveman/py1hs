weight = input("Enter weight of the parcel in kg: ")
try:
    weight = float(weight)
except ValueError:
    print("Invalid input. Please enter a valid number for weight.")
    exit()

if weight > 20:
    print("Too heavy (max 20kg)")
    exit()
elif weight <= 0:
    print("Invalid input. Please enter a valid weight greater than 0.")
    exit()


destination = input("Enter destination (bangkok, other): ").lower()
if destination not in ["bangkok", "other"]:
    print("Unknown destination.")
    exit()
express = input("Is it express delivery? (yes/no): ").lower()
outside_fee = 30

if weight <= 1:
    base_cost = 40
elif weight <= 5:
    base_cost = 80
elif weight <= 20:
    base_cost = 150

if destination != "bangkok":
    base_cost += outside_fee

if express == "yes":
    base_cost *= 2

print(f"Total cost: {base_cost:.2f} baht")