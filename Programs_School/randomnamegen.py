import random
from time import sleep
from typing import List
askrep = int(input("how many names should be generated?:\n"))
askinter = float(input("how fast should the names be shown? (recommanded are max 0.25 seconds between every gen!):\n"))

print("every name you want to add in the generator add in the according forename and/or surname list!\nLook in the program for comments!")

#to add forenames here: use 'foren.append("FORENAME HERE")' in one line for each
foren = list()
foren.append("Bob")
foren.append("John")
foren.append("Jan")
foren.append("Michael")
foren.append("Cedric")
foren.append("Markus")
foren.append("Frido")
foren.append("Loki")
foren.append("Maria")
foren.append("Elisabeth")
foren.append("Gisela")
foren.append("Monika")
foren.append("Renate")
foren.append("Klaus")
foren.append("Manfred")
#to add surnames here: use 'surn.append("SURNAME HERE")' in one line for each
surn = list()
surn.append("Johnson")
surn.append("Miller")
surn.append("Schmidt")
surn.append("Klein")
surn.append("Meyer")
surn.append("Jansen")
surn.append("Koch")
surn.append("Peters")
while askrep > 0:
    surname = random.choice(surn)
    forename = random.choice(foren)
    print(forename, surname)
    sleep(askinter)
    askrep = askrep - 1
    