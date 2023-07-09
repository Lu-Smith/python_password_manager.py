pwd = input("What is the master password? ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to quit, add a new password or view existing ones (quit/add/view )? ")

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "quit":
        break
    else:
        print("Invalid mode.")
        continue
