print("welcome to my game using if , else , elif ")
print("\n")
print("enter your desicion if you want to go inisde the forest type yes ")

d = input()

if d == "yes":
    print(" cheem kudak dam dam ")
    print(" welcome to the dark forest ")

    print("move forward to press m")

    d1 = input()

    if d1 == "m":
        print("mmmmm..... you are so brave ")

    else:
        print("no unfortunately you moved forwaard because this is my game my rules  ")

    print("there is a two path choose your path left or right ? ")

    d2= input()

    if d2=="left":
        print("oh noooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        print("there is a big kong ")

        print("fight or run ")

        d3= input()

        if d3=="fight":
            print("dishum dishum")
            print("you win ")

        elif d3=="run":
            print("you get a medal for worlds first androphobia")

        else : 
            print("sorry KONG win ")
    elif d2=="right":
        print("oh no there is lion ")
        print("you want climb a tree yes or no ")

        d4= input()

        if d4=="yes":
            print("you win a game ")

        elif d4=="no":
            print("lion : yummy food ")

        else : 
            print("lion : matikitaru orutharu ")
else : 
    print("go to house and sleep well")

