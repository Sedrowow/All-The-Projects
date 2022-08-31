def aRechteck(a1, a2):
    flaecheninhalt = a1 * a2
    print("flaecheninhalt: ", flaecheninhalt)
    return flaecheninhalt

def aQuadrat(seite):
    flaecheninhalt = aRechteck(seite, seite)
    return flaecheninhalt
    print("flaecheninhalt: ", flaecheninhalt)
    print(flaecheninhalt)
    

qor = int(input("1:Rechteck oder 2:Quadrat?:\n"))


if qor == 1:
    a1 = int(input("was ist die eine seite des Rechtecks?:\n"))
    a2 = int(input("was ist die andere Seite des Rechteks?:\n"))
    aRechteck(a1, a2)
elif qor == 2:
    seite = int(input("geben sie die Länge eiener Seite des Quadrats an:\n"))
    aQuadrat(seite)
else:
    print("Ungültige eingabe")