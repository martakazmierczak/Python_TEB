#Lab 3.1.1.4

n = int(input("Wprowadz liczbe: "))
print(n >= 100)

print()

#Lab 3.1.1.10

a = str(input("Wprowadź nazwę rośliny: "))
if a == "Skrzydłokwiat" :
    print("Skrzydłokwiat jest najlepszą rośliną w historii ")
    
else: 
    print("Nie, ja chcę Skrzydłokwiat!")
    
print()

#Lab 3.1.1.11

dochod = float(input("Wprowadź swój roczny dochód: "))
if dochod < 85528:
    podatek = (dochod * 0.18) -556.2 
else: 
    podatek = (dochod - 85528)*0.32 + 14839.2 
if podatek <0.0 :
    podatek = 0 

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)

#Lab 3.1.1.12

rok = int(input("Wprowadź rok: "))

if rok < 1582:
	print("nie w kalendarzu gregoriańskim")
else:
	if rok % 4 != 0:                #jeśli rok nie jest podzielny przez 4
		print("Rok zwykły")
	elif rok % 100 != 0:            #jeśli rok nie jest podzieln przez 100
		print("Rok przestępny")
	elif rok % 400 != 0:            #jeśli rok nie jest podzielny przez 400
		print("Rok zwykły")
	else:
		print("Rok przestępny") #inaczej rok przestępny

print()

#lab 3.2.1.3

tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

liczba = int(input("Wprowadz liczbę: "))

while liczba != tajny_numer:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    liczba = int(input("Wprowadź liczbe ponownie: "))
print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")

print()

#lab 3.2.1.6

import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
	
print("Ready or not, here I come!")

print()

#lab 3.2.1.9

słowo = str(input("Wprowadz slowo: "))
while True:
    slowo = input("Utknąłeś w pętli! Wpisz magiczne słowo, aby opuścić pętlę: ")
    if slowo == "pumpernikiel":
        break
print("Udało ci się opuścić pętlę.")

print()

#lab 3.2.1.10

slowo = input("Wprowadz slowo: ")
slowo = slowo.upper()

for litera in slowo:
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        print(litera)

print()

#lab 3.2.1.11

slowo_bez_samoglosek = ""

slowo = input("Wprowadź słowo: ")
slowo = slowo.upper()

for litera in slowo:
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        slowo_bez_samoglosek += litera
		
print(slowo_bez_samoglosek)
