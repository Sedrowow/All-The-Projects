import random
from typing import List
tries = 1
players = int(input("How many players? MAX players 4 \n"))
name = input("What's your name? main player?\n")
print("all players will have numbers so the name is just Decoration")
difficulty = int(input("Choose the difficulty! noob=1; the_average_player=2; The master_idiot_that_only_guesses_numbers=3"))
listplayer = players
human = list()
#numb is the random number that have to be guessed
if difficulty == 1:
    numb = random.randint(1,10)
elif difficulty == 2:
    numb = random.randint(1,100)
elif difficulty == 3:
    numb = random.randint(1,1000)
else:
    print("invalid difficulty, fallback to impossible mode muhaha")
    numb = random.randint(1,100000)


while players >= 1:
    if difficulty == 1:
        guess = False
        print("the number goes from 1 to 10")
        while guess == False:
            say = int(input("Please guess the number: "))
            if say == numb:
                print("You have guessed in", tries, "tries the right number! CONGRATS: \nPlayer", players)
                #man fügt doch hier append zum hinzufügen einer liste ein oder nicht?
                #Das Ziel war, die versuche abzuspeichern für den jeweiligen player...
                human.append(tries)
                guess = True
            else:
                if say < numb:
                    print("The Number needs to be higher")
                else:
                    print("The Number needs to be lower")
				#tries war hier an der falschen Stelle
                tries = tries + 1
    elif difficulty == 2:
        guess = False
        print("the number goes from 1 to 100")
        while guess == False:
            say = int(input("Please guess the number: "))
            if say == numb:
                print("You have guessed in", tries, "tries the right number! CONGRATS: \nPlayer", players)
                #man fügt doch hier append zum hinzufügen einer liste ein oder nicht?
                #Das Ziel war, die versuche abzuspeichern für den jeweiligen player...
                human.append(tries)
                guess = True
            else:
                if say < numb:
                    print("The Number needs to be higher")
                else:
                    print("The Number needs to be lower")
                tries = tries + 1
    if difficulty == 3:
        guess = False
        print("The number goes from 1 to 1000 have fun >:-)")
        while guess == False:
            say = int(input("Please guess the number: "))
            if say == numb:
                print("You have guessed in", tries, "tries the right number! CONGRATS \n Player", players, "\n(phew this did take very long... Doesn't it?)")
                #man fügt doch hier append zum hinzufügen einer liste ein oder nicht?
                #Das Ziel war, die versuche abzuspeichern für den jeweiligen player...
                human.append(tries)
                guess = True
            else:
                if say < numb:
                    print("The Number needs to be higher")
                else:
                    print("The Number needs to be lower")
                tries = tries + 1
    players = players - 1

while listplayer > 0:
    playnum = listplayer - 1
#Hier ist human.index nicht das was ich brauche, leider suchte ich vergeblich nach dem "command",
#der das macht was ich wollte: den bestimmten eintrag aus der liste abrufen

#du verwendest das Array falsch. index sucht nach einem bestimmten Eintrag. Du willst aber einen
#bestimmten Eintrag an einer bestimmten Stelle suchen. Die Korrektur sieht wie folgt aus
#    print("player", listplayer, "used", human.index(playnum), "tries")
    print("player", listplayer, "used", human.index(playnum), "tries")
    listplayer = listplayer - 1
    print("test")

#Anmerkungen: bei mehreren Spielern ist die Zufallszahl für alle Spieler gleich, da sie nur zum
#Beginn "ausgewürfelt wird