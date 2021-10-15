def start():
    print("Hi, welcome to this game!")
    print("Continue\n Y/N")

    option = input('')

    if option.lower() == 'y':
        print("What is your name?")
        name = input('')
        print(f"Hi {name}")


start()


def enter():
    print("ENTER the house🏠\n")
    option = input('')

    if option.lower() == 'enter':
        print(f"Welcome to the house {name}")

    else:
        print("You have entered the wrong key try again!")


enter()


def door():
    print("Choose a door")
    print("     1 🚪          2 🚪      ")
    option = input('')

    if option.lower() == '1':
        print("You have now entered room 1.")
        print()
    elif option.lower() == '2':
        print("You have now entered room 2.")


door()