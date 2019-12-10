# Installieren
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

# Importe
import mysql.connector

# Datenbank MySQL
DB_CBM = mysql.connector.connect(
  host="cbm.bremer-community.de",
  user="cbm",
  passwd="xmVx2_25",
  database="cbm_Autovermietung"
)

## Abfragen
# Übersicht über die vorhandenen Fahrzeuge
# Durch das eingeben vom Wort Fahrzeuge werden alle Fahrzeuge aufgelistet

# Menü 1
# Übersicht über die vorhandenen Fahrzeuge

mycursor = DB_CBM.cursor()
mycursor.execute("SELECT * FROM `autovermietung` WHERE `Fahrzeuge`")
myresult = mycursor.fetchall()

for x in myresult:
  print("Das sind alle Fahrzeuge: ", x)





# Menü 2
# Neue Fahrzeuge einfügen










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
