from datetime import datetime, timedelta
import json

# Dateien für Kurs- und Ferieninformationen sowie eigene Urlaubsplanung
dashboard_file = "./dashboard.json"
user_urlaub_file = "./user_urlaub.json"

# Kurs- und Ferieninformationen laden
def load_dashboard():
    try:
        with open(dashboard_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Kurs- und Ferieninformationen speichern
def save_dashboard(dashboard):
    with open(dashboard_file, "w") as file:
        json.dump(dashboard, file, indent=4)

# Eigene Urlaubsplanung laden
def load_user_urlaub():
    try:
        with open(user_urlaub_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Eigene Urlaubsplanung speichern
def save_user_urlaub(user_urlaub):
    with open(user_urlaub_file, "w") as file:
        json.dump(user_urlaub, file, indent=4)

# Lade alle Daten und kombiniere Kalenderdaten
def reload_calendar():
    global dashboard, user_urlaub, calendar
    dashboard = load_dashboard()
    user_urlaub = load_user_urlaub()
    calendar = {**dashboard, **user_urlaub}

# Initiales Laden
reload_calendar()

def check_date_status(date_input):
    try:
        # Eingabevalidierung
        date_obj = datetime.strptime(date_input, "%Y.%m.%d")
        if date_input in calendar:
            return f"Am {date_input} ist: {calendar[date_input]}"
        else:
            return f"Am {date_input} findet eine normale Kurswoche statt."
    except ValueError:
        return "Ungültiges Datum! Bitte geben Sie das Datum im Format 'Jahr.Monat.Tag' an (z.B. 2024.12.13)."

def check_today_status():
    today = datetime.now().strftime("%Y.%m.%d")
    print(check_date_status(today))

def add_urlaub_range(start_date, end_date, description):
    try:
        # Eingabevalidierung
        start_date_obj = datetime.strptime(start_date, "%Y.%m.%d")
        end_date_obj = datetime.strptime(end_date, "%Y.%m.%d")

        if start_date_obj > end_date_obj:
            print("Das Startdatum darf nicht nach dem Enddatum liegen.")
            return

        current_date = start_date_obj
        while current_date <= end_date_obj:
            formatted_date = current_date.strftime("%Y.%m.%d")
            user_urlaub[formatted_date] = description
            current_date += timedelta(days=1)

        save_user_urlaub(user_urlaub)
        reload_calendar()
        print(f"Urlaub hinzugefügt: {start_date} bis {end_date} - {description}")
    except ValueError:
        print("Ungültiges Datum! Bitte geben Sie die Daten im Format 'Jahr.Monat.Tag' an (z.B. 2024.12.13).")

def add_dashboard_entry(date_input, description):
    try:
        # Eingabevalidierung
        datetime.strptime(date_input, "%Y.%m.%d")
        dashboard[date_input] = description
        save_dashboard(dashboard)
        reload_calendar()
        print(f"Dashboard-Eintrag hinzugefügt: {date_input} - {description}")
    except ValueError:
        print("Ungültiges Datum! Bitte geben Sie das Datum im Format 'Jahr.Monat.Tag' an (z.B. 2024.12.13).")

def delete_entry(entry_type, date_input):
    try:
        if entry_type == "urlaub":
            if date_input in user_urlaub:
                del user_urlaub[date_input]
                save_user_urlaub(user_urlaub)
                reload_calendar()
                print(f"Urlaub am {date_input} wurde gelöscht.")
            else:
                print(f"Kein Urlaubseintrag für {date_input} gefunden.")
        elif entry_type == "dashboard":
            if date_input in dashboard:
                del dashboard[date_input]
                save_dashboard(dashboard)
                reload_calendar()
                print(f"Dashboard-Eintrag am {date_input} wurde gelöscht.")
            else:
                print(f"Kein Dashboard-Eintrag für {date_input} gefunden.")
        else:
            print("Ungültiger Eintragstyp. Bitte wählen Sie 'urlaub' oder 'dashboard'.")
    except ValueError:
        print("Ungültiges Datum! Bitte geben Sie das Datum im Format 'Jahr.Monat.Tag' an (z.B. 2024.12.13).")

def list_all_entries():
    print("\nAlle gespeicherten Einträge:")
    print("\nDashboard-Einträge:")
    for date, description in dashboard.items():
        print(f"{date}: {description}")

    print("\nUrlaubs-Einträge:")
    for date, description in user_urlaub.items():
        print(f"{date}: {description}")

# Hauptlogik
if __name__ == "__main__":
    print("Willkommen zum Kurs- und Ferienchecker!")
    print("Heutiger Status:")
    check_today_status()

    while True:
        print("\nOptionen:")
        print("1: Datum prüfen")
        print("2: Urlaub hinzufügen")
        print("3: Urlaub für einen Zeitraum hinzufügen")
        print("4: Dashboard-Eintrag hinzufügen")
        print("5: Eintrag löschen")
        print("6: Alle Einträge anzeigen")
        print("7: Beenden")
        choice = input("Bitte wählen Sie eine Option: ")

        if choice == "1":
            user_input = input("Bitte geben Sie ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")
            result = check_date_status(user_input)
            print(result)
        elif choice == "2":
            date_input = input("Bitte geben Sie das Datum des Urlaubs ein (Format: Jahr.Monat.Tag): ")
            description = input("Bitte geben Sie eine Beschreibung für den Urlaub ein: ")
            add_urlaub_range(date_input, date_input, description)
        elif choice == "3":
            start_date = input("Bitte geben Sie das Startdatum des Urlaubs ein (Format: Jahr.Monat.Tag): ")
            end_date = input("Bitte geben Sie das Enddatum des Urlaubs ein (Format: Jahr.Monat.Tag): ")
            description = input("Bitte geben Sie eine Beschreibung für den Urlaub ein: ")
            add_urlaub_range(start_date, end_date, description)
        elif choice == "4":
            date_input = input("Bitte geben Sie das Datum für den Dashboard-Eintrag ein (Format: Jahr.Monat.Tag): ")
            description = input("Bitte geben Sie eine Beschreibung für den Eintrag ein: ")
            add_dashboard_entry(date_input, description)
        elif choice == "5":
            entry_type = input("Welchen Eintrag möchten Sie löschen? (urlaub/dashboard): ")
            date_input = input("Bitte geben Sie das Datum des Eintrags ein (Format: Jahr.Monat.Tag): ")
            delete_entry(entry_type, date_input)
        elif choice == "6":
            list_all_entries()
        elif choice == "7":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")