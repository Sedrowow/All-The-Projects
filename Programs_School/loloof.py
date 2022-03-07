from time import sleep


counter = int(input("how much numbers you want to count?:\n"))
speed = float(input("how fast should the numebrs be count (0.5 half second):\n"))

while counter > 0:
    print(counter)
    counter = counter - 1
    sleep(speed)