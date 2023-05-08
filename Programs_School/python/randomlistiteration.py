import random
randomrangestart = int(input("Enter a startnumber for the randomgeneration: "))
randomrangeend = int(input("Enter an endnumber for the randomgeneration: "))
askamount = int(input("How many random numbers do you want to generate? "))
asklist = input("Do you want to create a list? (y/n) ")
asksort = input("Do you want to sort the list? (y/n) ")
askprintoutfile = input("Do you want to print the list to a file? (y/n) ")
listaddrandomstuff = input("Do you want to add random generated stuff to the list file (exmaple: names, age, date etc...)? (y/n) ")

def randomlist():
    randomlist = []
    for i in range(askamount):
        randomlist.append(random.randrange(randomrangestart, randomrangeend))
    return randomlist

if asklist == "y":
    if asksort == "y":
        print(sorted(randomlist()))
    else:
        print(randomlist())
elif asklist == "n":
    if askprintoutfile == "y":
        if asksort == "y":
            with open("randomlist.txt", "w") as file:
                file.write(str(sorted(randomlist())))
        else:
           with open("randomlist.txt", "w") as file:
                file.write(str(randomlist()))
        if listaddrandomstuff == "y":
            with open("randomlist.txt", "a") as file:
                file.write("\n")
                randamountadd = int(input("Enter amount of random strings to add to the list: "))
                for i in range(randamountadd):
                    file.write(str(random.randrange(randomrangestart, randomrangeend)))
                    file.write("\n")

    elif askprintoutfile == "n":
        if asksort == "y":
            print(sorted(randomlist()))
        else:
            print(randomlist())
    else:
        print("Invalid input")
else:
    print("Invalid input")
