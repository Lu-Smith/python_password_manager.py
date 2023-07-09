master_pwd = input("What is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n") 


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
