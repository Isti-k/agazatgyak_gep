
def feladat():
    Muzeum_neve=input("Kérlek, adj meg egy Múzeum nevet!")
    Latogato_neve=input("Kérlek, adja meg a látógató nevét!")
    Ertekeles=input("Kérem, adja meg az értékelést (1-20)-ig!:")

    Ertekeles=int(Ertekeles)

    if 1 <= Ertekeles <= 20:
        print("Köszönjük az értékelést!")
    elif Ertekeles <=0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif Ertekeles >20:
        print("20 pont feletti értékelés nem elfogadható!")




