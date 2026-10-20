angle01 = int(input("Enter the first angle of the triangle: "))
angle02 = int(input("Enter the second angle of the triangle: "))

angle03 = 180 - (angle01 + angle02)
if angle03 <= 0:
    print("The sum of the first two angles must be less than 180 degrees.")
else:
    print("The third angle of the triangle is:", angle03)   
