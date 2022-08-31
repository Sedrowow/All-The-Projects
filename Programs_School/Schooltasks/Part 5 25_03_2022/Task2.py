def BMI(gr,gew):
    erg = gr * gr
    bmi = gew / erg
    print("ihr BMI wert beträgt:", bmi)

def optipuls(age):
    optipuls = 165 - (0.75 * age)
    print("Alter:", age)
    print("Optimaler Puls:", optipuls)



def anhalteweg(speed):
    reaction = (speed / 10) * 3
    stopping = (speed / 10) * (speed / 10)
    length = reaction + stopping
    print("anhalteweg: ", length, "meter")


ask = int(input("1: BMI, 2: Optimaler Puls, 3: Anhalteweg:\n"))

if ask == 1:
    gr = int(input("Größe?:\n"))
    gew = int(input("Gewicht?:\n"))
    BMI(gr, gew)
elif ask == 2:
    age = int(input("wie alt sind sie?:\n"))
    optipuls(age)
elif ask == 3:
    speed = int(input("wie schnell ist das Auto (in Kmh)?:\n"))
    anhalteweg(speed)