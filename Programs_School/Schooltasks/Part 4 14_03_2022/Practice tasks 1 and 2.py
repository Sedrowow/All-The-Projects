def kontoundgebuehr(konto, gebuehr):
    zeit = konto / gebuehr
    print("Ihr kontostand ist nach",zeit, "monaten leer")


def Wachstum(Bestand, zielBestand, wachstum):
    jahre = 0
    wachstum = wachstum / 100
    while Bestand < zielBestand:
        jahre = jahre + 1
        Bestand = Bestand + Bestand * wachstum
    print("sie werden in", jahre, "Jahren Ihren zielbestand erreicht haben")

answer = int(input("wollen sie\n1:Ihren Kontostand mit Monatlichen Gebühren berechen?\n2: Ihren Kontostand mit einer Jährlichen Wachstumsrate zu einem Zielstand berechen?:\n>>"))


if answer == 1:
    konto = float(input("Wie viel Geld haben Sie auf ihrem Konto?:\n"))
    gebuehr = float(input("Wie viel Geld pro monat wird abgezogen?:\n"))

    kontoundgebuehr(konto, gebuehr)
elif answer == 2:
    Bestand = float(input("Geben sie ihren aktuellen Bestand ein:\n"))
    zielBestand = float(input("Geben sie ihren Ziel-Bestand ein:\n"))
    wachstum = int(input("Geben sie ihr Geld-Wachstum in prozent ein:\n"))
    Wachstum(Bestand, zielBestand, wachstum)
else:
    print("Ungültige Eingabe!")