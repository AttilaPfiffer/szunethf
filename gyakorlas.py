import random
import math
"""véletlen számok generálása"""
def veletlen():
    """10 és 30 közötti véletlen számok"""
    i: int = 0
    while i < 10:
        szam: int = math.floor(random.random() * 21 + 10)
        print(szam, end = " ")
        i += 1
        
"""1, Generálj 5 véletlen számot [1, 90]"""
def feladat1():
    print("1. feladat")
    i: int = 0
    while i < 5:
        szam:int = math.floor(random.random() * 91 + 1)
        print(szam, end = " ")
        i += 1



"""2, Generálj 1 véletlen kétjegyű egész számot, döntsd el, hogy páratlan vagy páros"""
def feladat2():
    print("2. feladat")
    i: int = 0
    while i < 1:
        szam:int = math.floor(random.random() * 100 + 10)
        if szam % 2 == 0:
            print(f"A {szam} páros!")
        else:
            print(f"A {szam} páratlan!")
        i += 1


"""3, Generálj 15 db egész számot [0, 1] között. Hány 1-est generáltál? """
def feladat3():
    print("3. feladat")
    i:int = 0
    while i < 15:
        szam:int = math.floor(random.random() * 2 + 0)
        print(szam, end = " ")
        i += 1



"""4, Generálj egy véletlen számot 1 és 10 között!. 
Vonj ki belőle 15-öt
Szorozd meg 3-mal
oszd el 6-tal
szorozd be 2-vel
Vond ki belőle az eredeti számot
A program írja ki, hogy az eredmény egyenlő-e 5-tel """



"""5, Írj metódust, mely a paraméterben kapott szövegnek kiírja a hosszát, az 5. karakterét nagybetűvel"""
