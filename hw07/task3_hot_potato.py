from collections import deque

names = input("Players (comma separated): ").split(",")
passes = int(input("Passes: "))

circle = deque(name.strip() for name in names)
out = []

while len(circle) > 1:
    for _ in range(passes):
        circle.append(circle.popleft())
    out.append(circle.popleft())

if out:
    print(", ".join(out) + " are out")
print("Winner: " + circle[0])