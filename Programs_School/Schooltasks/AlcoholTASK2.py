askalcalc = int(input("Was wollen sie berechnen? 1=Den reinalkoholgehalt in einem Bier? 2=Die Promile in ihrem Blut?"))


if askalcalc == 1:
    liter = float(input("Wie viel Liter Bier sollen berechnet werden?: "))
    percent = float(input("Wie viel prozent Alkohol sind in dem Bier?: "))
    percent = percent / 100.0
    
    end1 = liter * percent * 0.8
    print("in ihrem Bier sind", end1, "'%' reiner Alkohol enthalten.")
elif askalcalc == 2:
    drunk = float(input("Wie viel Gramm Alkohol haben sie zu sich genommen?: "))
    heavy = float(input("Wie viel Kilogramm wiegen sie?: "))
    prom = drunk / (0.65 * heavy)
    print ("promillegehalt=", prom, "%")
    if prom <= 0.3:
        print("Das geht ja noch...")
    elif prom <= 0.5 and prom > 0.3:
        print("ACHTUNG: BLOß NICHT MEHR AUTOFAHREN!!!")
    elif prom < 0.8 and prom > 0.5:
        print("Das ist schon etwas viel...")
    elif prom >= 0.8:
        print("Dazu gibt es kein Kommentar!")
    else:
        print("Irgendetwas ist schief gelaufen. Bitte fragen sie den Administrator für einen fix.")