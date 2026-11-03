RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]


def by_rating(r):
    return (-r[1], r[2])


def by_time(r):
    return (r[2], -r[1])


option = input("Sort by (rating/time): ").strip().lower()

if option == "rating":
    result = sorted(RESTAURANTS, key=by_rating)
elif option == "time":
    result = sorted(RESTAURANTS, key=by_time)
else:
    result = None

if result is None:
    print("Unknown option")
else:
    for i, r in enumerate(result, 1):
        print(str(i) + ". " + r[0] + ", " + str(r[1]) + " stars, " + str(r[2]) + " min")