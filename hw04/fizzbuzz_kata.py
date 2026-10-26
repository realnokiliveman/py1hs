number = int(input("Number: "))

fizz = number % 3 == 0 or "3" in str(number)
buzz = number % 5 == 0 or "5" in str(number)

if fizz and buzz:
    print("FizzBuzz")
elif fizz:
    print("Fizz")
elif buzz:
    print("Buzz")
else:
    print(number)