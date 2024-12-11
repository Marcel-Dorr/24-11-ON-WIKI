a = int(input("Bitte gebe die Erste Zahl ein: "))
b = int(input("Bitte gebe die Zweit Zahl ein: "))
# die Funktion input gibt die Erhaltenen Informationen als String aus und muss somit zu einem int konvertiert werden.
print("Wähle eine der folgenden Optionen:")
print("1. + Addition")
print("2. - Subtraktion")
print("3. * Multiplikation")
print("4. / Division")
choice = input("Geben Sie die Zahl der Auswahl ein (1-4): ")



if choice == "1":
    print(f"{a} + {b} = {a + b}")
elif choice == "2":
    result = {a - b}
    print(f"{a} - {b} = {a - b}")
elif choice == "3":
    result = {a * b}
    print(f"{a} * {b} = {a * b}")
elif choice == "4":
    result = {a / b}
    print(f"{a} / {b} = {a / b}")