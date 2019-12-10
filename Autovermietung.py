## Importe
import sqlite3

# Erstellt die Hauptdatenbank
datenbank = sqlite3.connect('Autovermietung.db')

# Mauszeiger holen
c = datenbank.cursor()

## Abfragen
# Übersicht über die vorhandenen Fahrzeuge
# Durch das eingeben vom Wort Fahrzeuge werden alle Fahrzeuge aufgelistet

# Übersicht über die vorhandenen Fahrzeuge
MP1=c.execute("""SELECT * FROM Fahrzeuge)""")

## Menü Fahrzeuge                               #Hauptmenü 0
#   |  
#   |- Fahrzeuge auflisten                      #1
#   |- Neue Fahrzeuge                           #2
#   |- Fahrzeuge entfernen                      #3
#   |- Fahrzeuge bearbeiten                     #4
#   |- Mietpreise für Fahrzeuge festlegen       #5
#   |- Sortierung der Fahrzeuge                 #6
#       |- Modell                               #7
#       |- Status                               #8
#           |- Vorhanden/Verliehen              #9
#   |- Mitarbeiter                              #10
#       |- Alle Mitarbeiter anzeigen            #11
#       |- Mitarbeiter anlegen
#       |- Mitarbeiter ändern
#   |- Kunde
#       |- Alle Kunden anzeigen
#       |- Neuer Kunde anlegen
#       |- Kunde ändern
#   |- Kundenoptionen
#       |- Fahrzeug leihen
#       |- Fahrzeug zurückbringen
#       |- Fahrzeug zustand
#           |- Fahrzeug beschädigt
#           |- Fahrzeug zerstört



print("Willkommen im Autovermietung Projekt in Python von Frank Panzer!")
print("Menü - Bitte wählen")
print("")
menu=input("")
