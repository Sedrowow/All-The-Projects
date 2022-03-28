import random
import time
from time import sleep
from typing import List

#FORENAMES: structure ist FORE.append("forename")
#SURNAMES: structure ist SUR.append("surname")
def foreandsurnames():
    FORE = list()
    FORE.append("John")
    FORE.append("Bob")
    FORE.append("Markus")
    FORE.append("Max")
    FORE.append("Cedrick")
    FORE.append("Michael")
    FORE.append("Jean")
    FORE.append("Bob")
    FORE.append("John")
    FORE.append("Jan")
    FORE.append("Michael")
    FORE.append("Cedric")
    FORE.append("Markus")
    FORE.append("Frido")
    FORE.append("Loki")
    FORE.append("Maria")
    FORE.append("Elisabeth")
    FORE.append("Gisela")
    FORE.append("Monika")
    FORE.append("Renate")
    FORE.append("Klaus")
    FORE.append("Manfred")
    
    forename = random.choice(FORE)
    
    SUR = list()
    SUR.append("Smith")
    SUR.append("Johnson")
    SUR.append("Miller")
    SUR.append("Schmidt")
    SUR.append("Klein")
    SUR.append("Meyer")
    SUR.append("Jansen")
    SUR.append("Koch")
    SUR.append("Peters")
    
    surname = random.choice(SUR)
    foransur = forename, surname
    return foransur


yourname = input("Hello User, whats your name?\n")
print("Welcome", yourname, ",")
task = int(input("You have 2 options: 1=Character Generator, or 2=a random name generator!"))

if task == 1:
    askhowname = int(input("how do you want to get your name? 1:generated 2:self written.: "))
    askhowage = int(input("how do you want to get your age? 1:generated 2:self written.: "))
    askhowclass = int(input("how do you want to get your class? 1:generated 2:self written.: "))
    if askhowname == 1:
        nameing = foreandsurnames()
        print("name:", nameing)
    elif askhowname == 2:
        print("Please write your name you made!")
        nameing = input("Your forename and surname: ")
    else:
        print("Wrong input, Fallback to name 'Some Guy'.")
        nameing = "Some Guy"
    
    if askhowage == 1:
        age = random.randint(18,80)
        print("age:", age)
    elif askhowage == 2:
        age = int(input("please type in your age:\n"))
    else:
        print("wrong input, fallback to a completely random age")
        age = random.randint(-1000,1000)
    if askhowclass == 1:
        print("Classgenerator not yet implemented!")
        classi = input("Please write the class by yourself")
    elif askhowclass == 2:
        classi = input("please type in your class:\n")
    else:
        print("invalid input! Fallback to 'i-can-nothing'")
        classi = "i-can-nothing"
    print("here is your character text:\n")
    print("My name is", nameing, ". I am", age, "years old and my class is:", classi)
if task == 2:
    askrep = int(input("how many names should be generated?:\n"))
    askinter = float(input("how fast should the names be shown? (recommended are max 0.25 seconds between every generation!):\n"))

    print("every name you want to add in the generator add to the according def!\nLook in the program for comments!")

    while askrep > 0:
        foreandsurnames()
        sleep(askinter)
        askrep = askrep - 1
