
#lab 2.1.1.6

print("Wlazl kotek na plotek")
print("Marta")

#lab 2.1.1.18
#slowa kluczowe sep, end

print("Kurs","Programowania","w", sep="***", end="...")
print("Pythonie")

#lab 2.1.1.19

#wersja 1
print("    * \n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
print()
print()

#wersja 2

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

print()
print()

#wersja 3

print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

print()
print()

#lab 2.2.1.11

print("\"Ucze sie\" \n \"\"jezyka\"\" \n \"\"\"Python\"\"\"")
print()
print()

#lab 2.4.1.7

pomaranczowy_krol = 3
agnieszka = 5
adam = 6
print(pomaranczowy_krol, agnieszka, adam, sep=",")
pomaranczy_razem = pomaranczowy_krol + agnieszka + adam
print(pomaranczy_razem)
print("Całkowita liczba pomaranczy: ", pomaranczy_razem)
print()
print()

#lab 2.4.1.9
kilometry = 12.25
mile = 7.38

mile_na_kilometry =  mile * 1.61
kilometry_na_mile =  kilometry /1.61

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")
print()
print()

# lab 2.4.1.10
x =  input("Wprowadz wartość: ")
x = float(x)
y = (3 * x **3) - (2 * x **2) + 3 * x - 1
print("y =", y)

# lab 2.5.1.2

#Ten program oblicza liczbę sekund w danej liczbie godzin.
#ten program został napisany dwa dni temu

godziny = 2 #liczba godzin
sekundy = 3600 #liczba sekund w 1 godzinie

print("Godzin: ", godziny) # wyświetla ilość godzin
print("Sekund w godzinach: ", godziny * sekundy)  # wyswietla ilość sekund w zadanej liczbie godzin
print()
print()
#tutaj powinniśmy również wyświetlić "Do widzenia", ale programista nie miał już na to czasu
# to jest koniec programu, który oblicza liczbę sekund w 3 godzinach

# lab2.6.1.9

a = float(input("Wprowadź wartość zmiennej a: "))
b = float(input("Wprowadź wartość zmiennej b: "))
print("dodawanie:", a + b)
print("odejmowanie:", a - b)
print("mnozenie:", a * b)
print("dzielenie:", a / b)
print("\nI to by było na tyle!")
print()
print()

#lab 2.6.1.10
x = float(input("Wprowadź wartość x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#lab 2.6.1.11
h = int(input("Czas rozpoczęcia (godziny): "))
m = int(input("Czas rozpoczęcia (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))
m = m + d
h = h + m // 60
m = m % 60
h = h % 24
print(h, ":", m, sep='')
print()
print()

# lab dodatkowe
kilometr = float(input("Wprowadz wartosc w kilometrach: "))
milimetr = float((kilometr)*1000000)
centymetr = float((kilometr)*100000)
metr = float((kilometr)*1000)
cal = float((kilometr)*39370)
stopy = float((kilometr)*3280)
mile = float((kilometr)/1.62)

print(kilometr," km to: ", milimetr, " mm")
print(kilometr," km to: ", centymetr, " cm")
print(kilometr," km to: ", metr, " m")
print(kilometr," km to: ", cal, " cal")
print(kilometr," km to: ", stopy, " stóp")
print(kilometr," km to: ", mile, " mi")

