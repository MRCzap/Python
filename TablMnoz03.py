# Program sprawdzający tabliczkę mnożenia
import time
import os
import random
czas = 0
ilpytan = 0
zakres = 0
ilbledow = 0
pytdodatkowe = 1
pytdodatkoweblad = 1
ilpytandodatkowych = 0
while czas < 5 or czas > 20:
    os.system('cls')
    czas = int(input("Podaj czas na odpowiedz (od 5 do 20 sekund): "))
while ilpytan < 2 or ilpytan > 50:
    os.system('cls')
    ilpytan = int(input("Podaj ilosc pytan (od 2 do 50 pytan): ")) 
while zakres < 1 or zakres > 10:
    os.system('cls')
    zakres = int(input("Podaj zakres tabliczki mnozenia: ")) 
while ilpytandodatkowych < 1 or ilpytandodatkowych > 20:
    os.system('cls')
    ilpytandodatkowych = int(input("Podaj maksymalna ilosc pytan dodatkowych (od 1 do 20): ")) 
os.system('cls')
print("Cwiczymy mnozenie z zakresu: ", zakres)
print("Na udzielenie odpowiedzi jest:", czas, " sekund")
print("Przekroczenie: ", czas, "sekund skutkuje dodaniem ",pytdodatkowe, " pytan")
print("Pytań jest ", ilpytan, " i każda pomyłka w odpowiedzi zwiększa ilość pytan o ", pytdodatkoweblad)
print ("Maksymalna ilosc pytan dodatkowych wynosi: ", ilpytandodatkowych)
print("")
null = input("Aby kontynuować naciśnij <ENTER> i <c> aby wyjsc:")
if null == "c": 
    quit()
while ilpytan:        
    print(" ")
    mnoznik = random.randrange(1, 10, 1)
    print("Ile to jest: ", zakres, " x ", mnoznik, " :")
    start = time.time()
    while True:
       try:
           wynik = int(input("Podaj wynik: "))
           break
       except ValueError:
           print("Nie wpisales zadnej wartosci...")
    stop = time.time()
    roznczas = int(stop - start)  
    if roznczas >= czas:
        ilbledow = ilbledow + 1
        print("Czas przekroczyl ", czas, " s")
        if ilpytandodatkowych > 0: 
            print(" Dodano ", pytdodatkowe, " pytan.")
            ilpytan = ilpytan + pytdodatkowe
            ilpytandodatkowych = ilpytandodatkowych - 1
        time.sleep(3)
    if (zakres*mnoznik) == wynik:
        print("Dobra odpowiedz!")
        print(" ")
        ilpytan = ilpytan - 1
    else:
        wynpopr = (zakres*mnoznik) 
        print(">>> ! - Zła odpowiedz! Powinno być: ", wynpopr)
        print("")
        ilbledow = ilbledow + 1
        if  ilpytandodatkowych > 0:
            print("Dodano ", pytdodatkowe, " pytan.")
            ilpytan = ilpytan + pytdodatkoweblad
            ilpytandodatkowych = ilpytandodatkowych - 1
        time.sleep(5)
    print("Zostało ", ilpytan, " pytan")
    print("")
print("Test zakonczony. Zrobiono: ", ilbledow, " bledow")
