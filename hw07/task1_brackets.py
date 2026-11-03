line = input()
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
problem = None

for i, ch in enumerate(line):
    if ch in "([{":
        stack.append((ch, i))
    elif ch in ")]}":
        if stack and stack[-1][0] == pairs[ch]:
            stack.pop()
        else:
            problem = (ch, i)
            break

if problem is None and stack:
    problem = stack[-1]

if problem is None:
    print("Balanced")
else:
    print("Problem at position " + str(problem[1]) + ": " + problem[0])
    print(line)
    print(" " * problem[1] + "^")