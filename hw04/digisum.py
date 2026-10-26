number = int(input("Number: "))
total = 0
while number > 0:
    total = total + number % 10
    number = number // 10
print("Digit sum:", total)