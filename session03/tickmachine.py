age = int(input("Age: "))
if age < 0 or age > 120:
    print("Invalid age. Please enter a valid age.")
    exit()
seat = input("Seat (normal/premium): ").lower()
if seat not in ["normal", "premium"]:
    print("Invalid seat type. Please enter 'normal' or 'premium'.")
    exit()
wknd = input("Weekend (yes/no): ").lower()
student_card = input("Student card (yes/no): ").lower()

price_normal = float(220)
price_premium = float(350)

if age < 12 or age > 60:
    price_normal = price_normal * 0.5
    price_premium = price_premium * 0.5

if student_card == "yes":
    price_normal = price_normal * 0.8
    price_premium = price_premium * 0.8

if wknd == "yes":
    price_normal = price_normal + 30
    price_premium = price_premium + 30

if seat == "normal":
    print(f"Total price: {price_normal:.2f} baht")
elif seat == "premium":
    print(f"Total price: {price_premium:.2f} baht")
