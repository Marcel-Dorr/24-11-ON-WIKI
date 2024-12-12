from datetime import datetime

# Funktion zur Eingabe von Alter (stellt sicher, dass die Eingabe eine ganze Zahl ist)
def get_age_input(person):
    while True:
        try:
            age = int(input(f"Gib das Alter von {person} ein: "))
            if age < 0:
                print("Das Alter kann nicht negativ sein. Versuch es noch einmal.")
                continue
            return age
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

# Berechnet die Differenz in Jahren zwischen zwei Alterswerten
def calculate_age_difference(age1, age2):
    return abs(age1 - age2)

# Berechnet die Anzahl der Tage, die eine Person schon lebt
def calculate_lived_days(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    birth_date = datetime(birth_year, 1, 1)  # Nehmen wir an, die Person hat an Neujahr Geburtstag
    today = datetime.today()
    lived_days = (today - birth_date).days
    return lived_days

# Hauptteil des Programms
def main():
    # Alter der beiden Personen abfragen
    age_person1 = get_age_input("Person 1")
    age_person2 = get_age_input("Person 2")

    # Zusammengezähltes Alter
    total_age = age_person1 + age_person2
    print(f"Das zusammengezählte Alter beider Personen ist: {total_age} Jahre.")

    # Alterdifferenz berechnen
    age_difference = calculate_age_difference(age_person1, age_person2)
    print(f"Der Altersunterschied zwischen den beiden Personen beträgt: {age_difference} Jahre.")

    # Lebenstage berechnen
    days_person1 = calculate_lived_days(age_person1)
    days_person2 = calculate_lived_days(age_person2)

    print(f"Person 1 hat bereits {days_person1} Tage gelebt.")
    print(f"Person 2 hat bereits {days_person2} Tage gelebt.")

# Das Skript ausführen
if __name__ == "__main__":
    main()