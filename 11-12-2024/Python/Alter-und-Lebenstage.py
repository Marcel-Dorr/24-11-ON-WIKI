import datetime

# Funktion zur Berechnung des Alters in Tagen
def berechne_alter(geburtsdatum):
    heute = datetime.date.today()
    alter_in_tagen = (heute - geburtsdatum).days
    alter_in_jahren = alter_in_tagen // 365  # Grobe Berechnung, ohne Schaltjahre zu berücksichtigen
    return alter_in_tagen, alter_in_jahren

# Eingabeaufforderungen
vorname = input("Bitte geben Sie Ihren Vornamen ein: ")
nachname = input("Bitte geben Sie Ihren Nachnamen ein: ")
geburtsdatum_str = input("Bitte geben Sie Ihr Geburtsdatum ein (JJJJ-MM-TT): ")

# Umwandlung des Geburtsdatums von String in ein datetime-Objekt
try:
    geburtsdatum = datetime.datetime.strptime(geburtsdatum_str, "%Y-%m-%d").date()
    
    # Berechnungen
    alter_in_tagen, alter_in_jahren = berechne_alter(geburtsdatum)
    
    # Ausgabe
    print(f"{vorname} {nachname}, Sie sind {alter_in_jahren} Jahre und {alter_in_tagen} Tage alt.")
except ValueError:
    print("Das eingegebene Geburtsdatum hat ein falsches Format. Bitte geben Sie es im Format JJJJ-MM-TT ein.")
