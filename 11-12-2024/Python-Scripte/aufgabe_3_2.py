note1 = int(input("Bitte gebe die Erste Note ein: "))
note2 = int(input("Bitte gebe die Zweit Note ein: "))
note3 = int(input("Bitte gebe die Dritte Note ein: "))
# die Funktion input gibt die Erhaltenen Informationen als String aus und muss somit zu einem int konvertiert werden.

print(f"{note1} + {note2} + {note3} = {(note1 + note2 + note3) / 3}")