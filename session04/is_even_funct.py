def is_even(n):

    if n % 2 == 0:
        return True
    else:
        return False

for i in range(1, 6):
    print(i, is_even(i))