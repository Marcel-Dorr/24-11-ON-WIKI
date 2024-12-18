import datetime

def aktuelles_datum_und_uhrzeit():
    now = datetime.datetime.now()
    print("Aktuelles Datum und Uhrzeit:", now.strftime("%d.%m.%Y %H:%M:%S"))

def tage_bis_jahresende():
    heute = datetime.date.today()
    jahresende = datetime.date(heute.year, 12, 31)
    differenz = jahresende - heute
    print(f"Tage bis zum Jahresende: {differenz.days} Tage")

def tage_bis_datum():
    while True:
        try:
            eingabe = input("Gib ein Datum im Format TT.MM.JJJJ ein: ")
            benutzer_datum = datetime.datetime.strptime(eingabe, "%d.%m.%Y").date()
            heute = datetime.date.today()
            differenz = benutzer_datum - heute
            print(f"Tage bis zum angegebenen Datum: {differenz.days} Tage")
            break
        except ValueError:
            print("Ungültiges Datum. Bitte versuche es erneut.")

def wochentag_berechnen():
    while True:
        try:
            eingabe = input("Gib ein Datum im Format TT.MM.JJJJ ein, um den Wochentag zu berechnen: ")
            benutzer_datum = datetime.datetime.strptime(eingabe, "%d.%m.%Y").date()
            wochentag = benutzer_datum.strftime("%A")
            print(f"Der Wochentag für {eingabe} ist {wochentag}.")
            break
        except ValueError:
            print("Ungültiges Datum. Bitte versuche es erneut.")

def zeit_in_zukunft():
    while True:
        try:
            eingabe = input("Gib eine Zeitspanne ein (Minuten, Stunden, Tage): ")
            zeitspanne = int(eingabe)
            einheit = input("Gib die Einheit ein (Minuten, Stunden, Tage): ").lower()
            jetzt = datetime.datetime.now()
            if einheit == "minuten":
                zukunft = jetzt + datetime.timedelta(minutes=zeitspanne)
            elif einheit == "stunden":
                zukunft = jetzt + datetime.timedelta(hours=zeitspanne)
            elif einheit == "tage":
                zukunft = jetzt + datetime.timedelta(days=zeitspanne)
            else:
                print("Ungültige Einheit. Bitte wähle 'Minuten', 'Stunden' oder 'Tage'.")
                continue

            print(f"In {zeitspanne} {einheit} wird es {zukunft.strftime('%d.%m.%Y %H:%M:%S')}.")
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

if __name__ == "__main__":
    aktuelles_datum_und_uhrzeit()
    tage_bis_jahresende()
    tage_bis_datum()
    wochentag_berechnen()
    zeit_in_zukunft()