import random
from time import sleep

play = True
print("Welcome to the game 21 (or former name Blackjack without money)!")
print("you will draw 2 cards now!")
no0 = "#####\n#  ##\n# # #\n##  #\n#####"
no1 = "    #\n    #\n    #\n    #\n    #"
no2 = "#####\n    #\n#####\n#    \n#####"
no3 = "#####\n    #\n#####\n    #\n#####"
no4 = "#   #\n#   #\n#####\n    #\n    #"
no5 = "#####\n#    \n#####\n    #\n#####"
no6 = "#####\n#    \n#####\n#   #\n#####"
no7 = "#####\n    #\n   # \n  #  \n #   "
no8 = "#####\n#   #\n#####\n#   #\n#####"
no9 = "#####\n#   #\n#####\n    #\n#####"
no10 = "    #/#####\n    #/#  ##\n    #/# # #\n    #/##  #\n    #/#####"
no11 = "    #/    #\n    #/    #\n    #/    #\n    #/    #\n    #/    #"
no12 = "    #/#####\n    #/    #\n    #/#####\n    #/#    \n    #/#####"
no13 = "    #/#####\n    #/    #\n    #/#####\n    #/    #\n    #/#####"
no14 = "    #/#   #\n    #/#   #\n    #/#####\n    #/    #\n    #/    #"
no15 = "    #/#####\n    #/#    \n    #/#####\n    #/    #\n    #/#####"
no16 = "    #/#####\n    #/    #\n    #/#####\n    #/#   #\n    #/#####"
no17 = "    #/#####\n    #/    #\n    #/   # \n    #/  #  \n    #/ #   "
no18 = "    #/#####\n    #/#   #\n    #/#####\n    #/#   #\n    #/#####"
no19 = "    #/#####\n    #/#   #\n    #/    #\n    #/#    \n    #/#####"
no20 = "#####/#####\n    #/#  ##\n#####/# # #\n#    /##  #\n#####/#####"
no21 = "#####/    #\n    #/    #\n#####/    #\n#    /    #\n#####/    #"
nobust = "0000 /0   0/ 000 /00000\n0  0 /0   0/0    /  0  \n000  /0   0/ 000 /  0  \n0  0 /0   0/    0/  0  \n0000 / 000 / 000 /  0  "

# 0000 0   0 000 00000
# 0  0 0   00      0  
# 000  0   0 000   0  
# 0  0 0   0    0  0  
# 0000  000  000   0 
cardpc = 0 
draw = True
card = 0
card = card + random.randint(1,10)
while play == True:
    card = 0
    cardpc = 0 
    draw = True
    card = card + random.randint(1,10)
    while draw == True:
        card = card + random.randint(1,10)
        if card == 0:
            print("your card points are:\n", no0)
        elif card == 1:
            print("your card points are:\n",no1)
        elif card == 2:
            print("your card points are:\n",no2)
        elif card == 3:
            print("your card points are:\n",no3)
        elif card == 4:
            print("your card points are:\n",no4)
        elif card == 5:
            print("your card points are:\n",no5)
        elif card == 6:
            print("your card points are:\n",no6)
        elif card == 7:
            print("your card points are:\n",no7)
        elif card == 8:
            print("your card points are:\n",no8)
        elif card == 9:
            print("your card points are:\n",no9)
        elif card == 10:
            print("your card points are:\n",no10)
        elif card == 11:
            print("your card points are:\n",no11)
        elif card == 12:
            print("your card points are:\n",no12)
        elif card == 13:
            print("your card points are:\n",no13)
        elif card == 14:
            print("your card points are:\n",no14)
        elif card == 15:
            print("your card points are:\n",no15)
        elif card == 16:
            print("your card points are:\n",no16)
        elif card == 17:
            print("your card points are:\n",no17)
        elif card == 18:
            print("your card points are:\n",no18)
        elif card == 19:
            print("your card points are:\n",no19)
        elif card == 20:
            print("your card points are:\n",no20)
        elif card == 21:
            print("your card points are:\n",no20)
        else:
            print("your card points are over 21:\n",nobust)
        
        
        if card >= 21:
            if card == 21:
                print("you won!")
                play = False
                draw = False
            elif card > 21:
                print("You lost")
                play = False
                draw = False
        if card < 21:
            drawask = input("draw again? y = yes, n = no")
            if drawask == "y":
                draw = True
            else:
                draw = False
                print("computers turn!")
                #card Computer Turn
                cardpct = True
                #card amount of pc and first draw
                cardpc = 0
                cardpc = cardpc + random.randint(2,10)
                while cardpct == True:
                    cardpc = cardpc + random.randint(2,10)
                    if cardpc == 0:
                        print("Pcs card points are:\n", no0)
                    elif cardpc == 1:
                        print("Pcs card points are:\n",no1)
                    elif cardpc == 2:
                        print("Pcs card points are:\n",no2)
                    elif cardpc == 3:
                        print("Pcs card points are:\n",no3)
                    elif cardpc == 4:
                        print("Pcs card points are:\n",no4)
                    elif cardpc == 5:
                        print("Pcs card points are:\n",no5)
                    elif cardpc == 6:
                        print("Pcs card points are:\n",no6)
                    elif cardpc == 7:
                        print("Pcs card points are:\n",no7)
                    elif cardpc == 8:
                        print("Pcs card points are:\n",no8)
                    elif cardpc == 9:
                        print("Pcs card points are:\n",no9)
                    elif cardpc == 10:
                        print("Pcs card points are:\n",no10)
                    elif cardpc == 11:
                        print("Pcs card points are:\n",no11)
                    elif cardpc == 12:
                        print("Pcs card points are:\n",no12)
                    elif cardpc == 13:
                        print("Pcs card points are:\n",no13)
                    elif cardpc == 14:
                        print("Pcs card points are:\n",no14)
                    elif cardpc == 15:
                        print("Pcs card points are:\n",no15)
                    elif cardpc == 16:
                        print("Pcs card points are:\n",no16)
                    elif cardpc == 17:
                        print("Pcs card points are:\n",no17)
                    elif cardpc == 18:
                        print("Pcs card points are:\n",no18)
                    elif cardpc == 19:
                        print("Pcs card points are:\n",no19)
                    elif cardpc == 20:
                        print("Pcs card points are:\n",no20)
                    elif cardpc == 21:
                        print("Pcs card points are:\n",no21)
                    else:
                        print("Pcs card points are over 21:\n",nobust)
                    sleep(1)
                    
                    if cardpc >= 21:
                        if cardpc == 21:
                            print("PC won, his card numbers are:\n", no21)
                            cardpct = False
                        else:
                            print("PC lost, his card numbers are over 21:\n",nobust)
                            cardpct = False
                        cardpct = False
    
                    if cardpc < 21:
                        if cardpc < 17:
                            cardpct = True
                        else:
                            cardpct = False
                            if cardpc == 0:
                                print("Pcs card points are:\n", no0)
                            elif cardpc == 1:
                                print("Pcs card points are:\n",no1)
                            elif cardpc == 2:
                                print("Pcs card points are:\n",no2)
                            elif cardpc == 3:
                                print("Pcs card points are:\n",no3)
                            elif cardpc == 4:
                                print("Pcs card points are:\n",no4)
                            elif cardpc == 5:
                                print("Pcs card points are:\n",no5)
                            elif cardpc == 6:
                                print("Pcs card points are:\n",no6)
                            elif cardpc == 7:
                                print("Pcs card points are:\n",no7)
                            elif cardpc == 8:
                                print("Pcs card points are:\n",no8)
                            elif cardpc == 9:
                                print("Pcs card points are:\n",no9)
                            elif cardpc == 10:
                                print("Pcs card points are:\n",no10)
                            elif cardpc == 11:
                                print("Pcs card points are:\n",no11)
                            elif cardpc == 12:
                                print("Pcs card points are:\n",no12)
                            elif cardpc == 13:
                                print("Pcs card points are:\n",no13)
                            elif cardpc == 14:
                                print("Pcs card points are:\n",no14)
                            elif cardpc == 15:
                                print("Pcs card points are:\n",no15)
                            elif cardpc == 16:
                                print("Pcs card points are:\n",no16)
                            elif cardpc == 17:
                                print("Pcs card points are:\n",no17)
                            elif cardpc == 18:
                                print("Pcs card points are:\n",no18)
                            elif cardpc == 10:
                                print("Pcs card points are:\n",no19)
                            elif cardpc == 20:
                                print("Pcs card points are:\n",no20)
                            else:
                                print("someting went wrong!!!!")
                        
                            if card < cardpc:
                                print("You lost! The pc has more points")
                            elif card > cardpc:
                                print("You won! You have more points")
                            else:
                                print("It's a draw! Phew... that was close!")
                        
                            
                                
    playask = input("want to play again? y = yes, n = no")
    if playask == "y":
        play = True
    else:
        play = False