from datetime import datetime

# Funktion zur Eingabe von Alter (stellt sicher, dass die Eingabe eine ganze Zahl ist)
def get_age_input(person_name):
    while True:
        try:
            age = int(input(f"Gib das Alter von {person_name} ein: "))
            if age < 0:
                print("Das Alter kann nicht negativ sein. Versuch es noch einmal.")
                continue
            return age
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

# Funktion zur Eingabe des Namens einer Person
def get_name_input(person_number):
    while True:
        name = input(f"Gib den Namen von Person {person_number} ein: ").strip()
        if name:
            return name
        else:
            print("Der Name darf nicht leer sein. Versuch es noch einmal.")

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
    # Namen der Personen abfragen
    name_person1 = get_name_input(1)
    name_person2 = get_name_input(2)

    # Alter der beiden Personen abfragen
    age_person1 = get_age_input(name_person1)
    age_person2 = get_age_input(name_person2)

    # Zusammengezähltes Alter
    total_age = age_person1 + age_person2
    print(f"Das zusammengezählte Alter von {name_person1} und {name_person2} ist: {total_age} Jahre.")

    # Altersdifferenz berechnen
    age_difference = calculate_age_difference(age_person1, age_person2)
    print(f"Der Altersunterschied zwischen {name_person1} und {name_person2} beträgt: {age_difference} Jahre.")

    # Lebenstage berechnen
    days_person1 = calculate_lived_days(age_person1)
    days_person2 = calculate_lived_days(age_person2)

    print(f"{name_person1} hat bereits {days_person1} Tage gelebt.")
    print(f"{name_person2} hat bereits {days_person2} Tage gelebt.")

# Das Skript ausführen
if __name__ == "__main__":
    main()