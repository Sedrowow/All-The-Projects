from typing import List
import random
import time
name = int(input("Wie wollen sie die namen generieren? 1=alles gleich (schreiben); 2=automatisch"))

FORE = list()
FORE.append("John")
FORE.append("Bob")
FORE.append("Markus")
FORE.append("Maximilian")
FORE.append("Cedrick")
FORE.append("Sedrick")
FORE.append("Michael")
FORE.append("Lea")
FORE.append("Jan")


SUR = list()
SUR.append("Fanderl")
SUR.append("Smith")
SUR.append("Fischer")
SUR.append("Schönlau")
SUR.append("Zoller")
SUR.append("Bloxberg")

if name == 1:
    askname = input("Welchen Namen wollen sie wiederholen?")
    repeat = int(input("Wie oft soll Ihr Name Wiederholt werden?: "))
    while repeat > 0:
        print(askname)
        repeat = repeat - 1

elif name == 2:
    repeat = int(input("Wie oft sollen die generierten namen wiederholt werden?"))
    while repeat > 0:
        fname = random.choice(FORE)
        sname = random.choice(SUR)
        print(fname, sname)
        time.sleep(0.05)
        repeat = repeat - 1