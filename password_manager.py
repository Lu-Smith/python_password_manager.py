pwd = input("What is the master password? ")

while True:
    mode = input("Would you like to quit, add a new password or view existing ones (quit/add/view )? ")

    if mode == "view":
        pass
    elif mode == "add":
        pass
    elif mode == "quit":
        quit()
    else:
        print("Invalid mode.")
        continue
