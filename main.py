
number = int(input("Bitte geben Sie eine Zahl zur Überprüfung auf Primzahl ein: "))

divisors = []

for i in range(1, number):
    if number % i == 0 and i != 1 and i != number:
        divisors.append(i)

if len(divisors) == 0:
    print("Die Zahl ist eine Primzahl")
else:
    print("Die Zahl ist keine Primzahl, Teiler der Zahl sind: ")
    print(*divisors, sep=", ")
