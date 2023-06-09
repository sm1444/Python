print("Welcome to the game menu")
print("Enter 1 for game 1")
print("Enter 2 for game 2")
print("Enter 3 to quit")

game = int(input("Enter your choice: "))
mode = 0
multi = 0
map = 0

if game==1:
    print("Welcome to game 1")
    print("Enter 1 for solo mode")
    print("Enter 2 for multiplayer mode")
    mode = int(input("Enter mode: "))
    if mode == 1:
        print("Welcome to solo mode...Let's start playing")
    elif mode == 2:
        print("Enter 1 to play with friends")
        print("Enter 2 to play online")
        multi = int(input("Enter multiplayer mode: "))
        if multi == 1:
            print("Share the code XXXXX with friends to start playing")
        elif multi == 2:
            print("Searching for a local server... let's start playing")
        else:
            print("Enter a valid choice.")
    else:
        print("Enter a valid choice")

elif game == 2:
    print("Welcome to game 2")
    print("Enter 1 for solo mode")
    print("Enter 2 for multiplayer mode")
    mode = int(input("Enter mode: "))
    if mode == 1:
        print("Welcome to solo mode...Let's start playing")
        print("Enter 1 for map 1")
        print("Enter 2 for map 2")
        print("Enter 3 for map 3")
        map = int(input("Enter the choice of map: "))
        if map == 1:
            print("Welcome to map 1")
        elif map == 2:
            print("Welcome to map 2")
        elif map==3:
            print("Welcome to map 3")
        else:
            print("Enter a valid choice")
    elif mode == 2:
        print("Enter 1 to play with friends")
        print("Enter 2 to play online")
        multi = int(input("Enter multiplayer mode: "))
        if multi == 1:
            print("Share the code XXXXX with friends to start playing")
            print("Enter 1 for map 1")
            print("Enter 2 for map 2")
            print("Enter 3 for map 3")
            map = int(input("Enter the choice of map: "))
            if map == 1:
                print("Welcome to map 1")
            elif map == 2:
                print("Welcome to map 2")
            elif map==3:
                print("Welcome to map 3")
            else:
                print("Enter a valid choice")
        elif multi == 2:
            print("Searching for a local server... let's start playing")
            print("Enter 1 for map 1")
            print("Enter 2 for map 2")
            print("Enter 3 for map 3")
            map = int(input("Enter the choice of map: "))
            if map == 1:
                print("Welcome to map 1")
            elif map == 2:
                 print("Welcome to map 2")
            elif map==3:
                print("Welcome to map 3")
            else:
                print("Enter a valid choice")
        else:
            print("Enter a valid choice.")
    else:
        print("Enter a valid choice")

elif game == 3:
    print("Thank you for playing.")
else:
    print("Enter a valid number")