#this program is made for schoolwork
#WRITTEN IN GERMAN
import random
from typing import List

askhor = int(input("Bitte geben sie ihre Horoskop nummer ein! 1=Steinbock, 2=Waage, 3=Widder: "))

#THIS IS A LIST FOR THE RANDOM GENERATOR FOR INVALID INPUTS!

ADJEC = list()
ADJEC.append("freundliche")
ADJEC.append("glückliche")
ADJEC.append("schlechte")
ADJEC.append("unbestimmte")

NOUN1 = list()
NOUN1.append("Zukunft")
NOUN1.append("Eigenschaft")
NOUN1.append("Einstellung")

TIMES = list()
TIMES.append("immer")
TIMES.append("oft")
TIMES.append("selten")
TIMES.append("manchmal")
TIMES.append("niemals")

FEELING = list()
FEELING.append("glücklich")
FEELING.append("unfreundlich")
FEELING.append("böse")
FEELING.append("unachtsam")

#I am not shure which horoscope is the latest rn, so i made some up!

if askhor == 1:
    print("Sie haben vieles schon geschafft, doch sie haben langsam keine lust mehr. Motivation wird bei Ihnen stark benötigt!")
elif askhor == 2:
    print("Sie sind ein sehr netter Mensch, doch falls Sie von jemanden geärgert werden, werden sie Böse...")
elif askhor == 3:
    print("Sowohl Hass als auch liebe hat Ihr Leben durcheinander gebracht, doch Ihr standfestes Gedächtnis hält sie am leben dran.")
else:
    print("kein Gültges Sternzeichen, schreibe ein zufälliges horoskop")
    adj = random.choice(ADJEC)
    non1 = random.choice(NOUN1)
    time = random.choice(TIMES)
    feel = random.choice(FEELING)
    print("Ihre", adj, non1, "Führt dazu, dass sie", time, feel, "sind.")