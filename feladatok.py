def feladat1():
    print("1. feladat")
    print("Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!")
    szam = int(input("Kérem adjon meg egy olyan számot ami 200 és 900 között van: "))
    if 200 <= szam <= 920:
        elso_szamjegy = int(str(szam)[0])
        print("A szám első számjegye: " + str(elso_szamjegy))
    else:
        print("Hibát! A megadott szám nincs a 200 és 900 között")

def feladat2():
    print("2. feladat")
    print("Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre.")
    osszeg = 0
    szam: int = int(input("Adjon meg egy számot: "))
    while szam > 0:
        osszeg += szam % 10  
        szam //= 10  
    print("A számjegyek összege: " + str(osszeg))

def feladat3():
    print("3. feladat")
    print("A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!")
    szam: float = float(input("Adjon meg egy valós számot: "))
    while (szam >= 0):
        szam_gyok = szam ** 0.5
        print(f"A {szam} négyzetgyöke: {szam_gyok}")
        break
    else:
        print("Negatív szából nem lehet gyököt vonni!")
    
def feladat4():
    print("4. feladat")
    print("A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! ")
    a: int = int(input("Adjon meg egy számot (ez lesz az egyik oldal): "))
    b: int = int(input("Adjon meg egy másik számot (ez lesz a másik oldal): "))
    while (a > 0 and b > 0):
        kerulet = 2 * (a + b)
        terulet = a * b
        print("A téglalap kerulete: " + str(kerulet))
        print("A téglalap terulete: " + str(terulet))
        break
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")

def feladat5():
    print("5. feladat")
    print("Írj metódust, ami paraméterében kap két számot, és kiírja a két szám legnagyobb közös osztóját!")
    szam1: int = int(input("Adjon meg egy számot: "))
    szam2: int = int(input("Adjon meg egy másik számot: "))
    while szam2:
        szam1, szam2 = szam2, szam1 % szam2
    print("A két szám legnagyobb közös osztója: " + str(szam1))

def szam_szamjegyek(szam:int):
    print("szam: ", szam)
    """Hogy kapjuk meg az utolsó számjegyet?"""
    while (szam > 9):
        print("következő számjegy", szam % 10)
        szam = szam // 10
        print("Az aktuális szám: ", szam)
    print("Az utolsó számjegy: ", szam)

def szam_jegyek2(szam: int):
    szoveg_szam: str = str(szam)
    i = 0
    while i < len(szoveg_szam):
        print(szoveg_szam[i])
        i += 1

def ermedobas():
    i: int = 0
    f_szama: int = 0
    f_hossz:int = 0
    max_hossz:int = 0
    elozo_string_f = False
    while i < 10:
        jel: str = input("Adj meg egy jelet (F/I): ")
        while not((jel == "F") or (jel == "f") or (jel == "I") or (jel == "i")):
            jel: str = input("Nem jó,  (F/I)-t adj meg: ")

        if (jel == "f" or jel == "F"):
            f_szama += 1
            fhossz += 1
            elozo_string_f = True
        else:
            print("Aktuális hossz: ", fhossz)
            elozo_string_f = False
            if (max_hossz < f_hossz):
                max_fhossz = f_hossz
            f_hossz = 0    
        i += 1

    print("Aktuális hossz: ", fhossz)
    if (max_hossz < f_hossz):
        max_fhossz = f_hossz
    print("F-ek száma: ", f_szama)
    print("Maximális hossz: ", max_hossz)
