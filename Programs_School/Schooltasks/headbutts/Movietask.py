
import sys


print("each saved file is a sesion!")
newfile = int(input("do you want to: 1=make a new file, 2=read a file, 3=Add sth to a file or 4= delete a file?"))

if newfile == 1:
    filename = input("What name should the file have?:\n")
    DD = input("Which DAY (of the month) should the session be?:\n")
    MM = input("Which MONTH (in numbers) will be the session?:\n")
    YYYY = input ("Which year (4 DIGITS: example 2022) will  be te session?:\n")
    HH = input("On which hour will be the session?:\n")
    MIN = input("On which Minute will be the session:\n")
    ROWS = int(input("how many rows are in the session?:\n"))
    SEATS = int(input("how much seats per row are there?:\n"))
    OOFIMAN = SEATS
    
    file = open(f"{filename}.txt", 'w')
    while ROWS > 0:
        while OOFIMAN > 0:
            sys.stdout.write("#")
            OOFIMAN = OOFIMAN - 1
        OOFIMAN = SEATS
        print("")
        ROWS = ROWS - 1