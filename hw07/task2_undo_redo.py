undo_stack = []
redo_stack = []

while True:
    command = input("type/undo/redo/quit: ").strip().lower()

    if command == "quit":
        break
    elif command == "type":
        text = input("Text: ")
        undo_stack.append(text)
        redo_stack.clear()
        print("Document: " + "".join(undo_stack))
    elif command == "undo":
        if undo_stack:
            redo_stack.append(undo_stack.pop())
            print("Document: " + "".join(undo_stack))
        else:
            print("Nothing to undo")
    elif command == "redo":
        if redo_stack:
            undo_stack.append(redo_stack.pop())
            print("Document: " + "".join(undo_stack))
        else:
            print("Nothing to redo")