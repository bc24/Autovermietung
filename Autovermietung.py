'''
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Installieren
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

Quellen
Menü              -   http://effbot.org/tkinterbook/menu.htm
MySQL Connector   -   https://pypi.org/project/mysql-connector-python/

'''
# Importe
import mysql
import mysql.connector
from tkinter import *
import time
import sys

# Datenbank MySQL
DB_CBM = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "cbm_Autovermietung"
)
mycursor = DB_CBM.cursor()

"""
# Datenbank erstellen Start

# SQL Tabelle mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS mitarbeiter(mitarbeiter_id INTEGER PRIMARY KEY AUTOINCREMENT,vorname VARCHAR(30),nachname VARCHAR(50),strasse VARCHAR(80),hausnummer INTEGER,plz_id INTEGER,telefonnr VARCHAR(80),FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") #IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle zweigstellen erstellen
mycursor.execute("CREATE TABLE zweigstellen (standort_id INTEGER PRIMARY KEY AUTOINCREMENT,strasse VARCHAR(80),plz_id INTEGER,hausnummer INTEGER,telefonnr INTEGER,steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle zweigstellen_mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstellen_mitarbeiter(standort_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (standort_id) REFERENCES standorte(standort_id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle kunde erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS kunden(kunden_id INTEGER PRIMARY KEY AUTOINCREMENT, vorname VARCHAR(30), nachname VARCHAR(50), strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(80), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle fahrzeuge erstellen
mycursor.execute("CREATE TABLE fahrzeuge(kfz_id INTEGER PRIMARY KEY AUTOINCREMENT,marke VARCHAR(50),modell VARCHAR(50),status VARCHAR(30),kennzeichen VARCHAR(11),standort_id INTEGER, kfz_preis_id INTEGER,FOREIGN KEY (standort_id) REFERENCES standorte(standort_id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (kfz_preis_id) REFERENCES kfr_preis(kfz_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle plz_id erstellen
mycursor.execute("CREATE TABLE plz_id (plz_id INTEGER PRIMARY KEY AUTOINCREMENT,plz CHAR(5), ort varchar(50))") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# Datenbank erstellen Stop
"""

# Übersicht über die vorhandenen Fahrzeuge

def FahrzeugeAnzeigen():
  mycursor = DB_CBM.cursor()
  mycursor.execute("SELECT * FROM fahrzeuge")
  myresult = mycursor.fetchall()

  #for x in myresult:
  #  print("Das sind alle Fahrzeuge: ", x)


# Neue Fahrzeuge einfügen

def FahrzeugeAnlegen():
  Fahrzeuge_Anlegen1=input("Bitte geben Sie eine Fahrzeugmarke ein, die Sie hinzufügen wollen: ")
  Fahrzeuge_Anlegen2 = input("Bitte geben Sie eine Fahrzeugmodell ein, die Sie hinzufügen wollen: ")
  Fahrzeuge_Anlegen3 = input("Bitte geben Sie an ob das Auto zu verfügung steht(1) oder Nicht zu verfügung steht(0): ")

  mycursor = DB_CBM.cursor()

  # ID für Fahrzeug wird gehollt
  res= mycursor.execute("INSERT INTO fahrzeuge (fahrzeug_id) VALUES (%s)", (Fahrzeuge_Anlegen,))
  print(res.lastinsertid)
  fzid = res.lastinsertid

# Fahrzeug Dummy nur erzeugen wenn kein Datensatz zuverfügung steht
  #mycursor.execute("INSERT INTO `fahrzeuge` (`fahrzeug_id`, `marke`, `modell`, `status`, `kennzeichen`, `zweigstelle_id`, `kfz_preis_id`) VALUES (NULL, 'bmw', '3er', 'da', 'hb-fp-103', '2', '250');)

  mycursor.execute("UPDATE fahrzeuge SET (fahrzeug_id) WHERE fahrzeug_id ="+ fzid + (Fahrzeuge_Anlegen0,))
  mycursor.execute("INSERT INTO fahrzeuge (marke) VALUES (%s)", (Fahrzeuge_Anlegen1,))
  mycursor.execute("INSERT INTO fahrzeuge (modell) VALUES (%s)", (Fahrzeuge_Anlegen2,))
  mycursor.execute("INSERT INTO fahrzeuge (status) VALUES (%s)", (Fahrzeuge_Anlegen3,))

  # marke, modell, status, kennzeichen, zweigstelle_id, kfz_preis_id
  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)

def menuepunkt3():
  Fahrzeuge_Anlegen=input("Bitte geben Sie eine Automarkte ein die Sie hinzufügen wollen: ")
  mycursor = DB_CBM.cursor()
  mycursor.execute("INSERT INTO fahrzeuge (fahrzeugmarken) VALUES (%s)", (Fahrzeuge_Anlegen,) )
  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)


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
#       |- Vorhanden                            #9              ###### Weiter Bearbeiten
#       |- Verliehen                            #10
#   |- Mitarbeiter                              #11
#       |- Alle Mitarbeiter anzeigen            #12
#       |- Mitarbeiter anlegen                  #13
#       |- Mitarbeiter ändern                   #14
#   |- Kunde                                    #15
#       |- Alle Kunden anzeigen                 #16
#       |- Neuer Kunde anlegen                  #17
#       |- Kunde ändern                         #18
#   |- Kundenoptionen                           #19
#       |- Fahrzeug leihen                      #20
#       |- Fahrzeug zurückbringen               #21
#       |- Fahrzeug zustand                     #22
#           |- Fahrzeug beschädigt              #23
#           |- Fahrzeug zerstört                #24


# Abfrage kunde oder Mitarbeiter
print("Sind sie Kunde(1) oder Mitarbeiter(2)? ")
Frage1 = input()

print("Bitte geben sie ihren Vornamen ein: ")
Vorname = input()

print("Bitte geben sie ihren Nachnamen ein: ")
Nachname = input()

# Wenn Kunde dann
if Frage1 == "1":
  print("Guten Tag Herr/Frau", Nachname + "! Sind Sie Neu(1) oder sind Sie schon Kunde(2)? ")
  kunde1 = input()
  if kunde1 == "1":  # Kunde anlegen
    Nachname = input()
    liste_kunde = []
    liste_kunde.insert(0, Nachname)
    liste_kunde.insert(1, Vorname)
    print("Bitte geben Sie ihre Strasse: ")
    Strasse = input()
    liste_kunde.insert(2, Strasse)
    print("Bitte geben sie ihre Hausnummer ein:")
    Hausnummer = input()
    liste_kunde.insert(3, Hausnummer)
    print("Bitte geben sie ihre Postleitzahl ein:")
    plz = []
    plz = input()
    liste_kunde_plz.insert(0, plz)
    print("Bitte geben Sie ihren Wohnort ein:")
    Ort = input()
    liste_kunde_plz.insert(1, Ort)
    print("Bitte geben sie ihre Telefonnummer im Format 0421123456 (Also ohne Lehrzeichen,+ oder -)")
    Telefon = input()
    liste_kunde.insert(4, Telefon)
    tupel_kunde = (liste_kunde)
    tupel_kunde_plz = (liste_kunde_plz)
    cursor.execute("""INSERT INTO kunden (nachname, vorname, strasse, hausnummer, telefonnr) VALUES (?,?,?,?,?)""",
                   (tupel_kunde))
    cursor.execute("""INSERT INTO plz_id (plz, ort) VALUES (?,?)""", (tupel_kunde_plz))
    connection.commit()
    print("Sie haben folgende Daten eingegeben. Bitte merken sie sich ihre Kundennummer!")
    sql = "SELECT * FROM kunden"
    print(sql)

  if Frage1 == "2":
    print("Bitte geben sie ihre Kundennummer ein:")


### Mitarbeiter
if Frage1 == "2":
  print("Willkommen zurück Herr/Frau", Nachname + "!")
  print("Hallo", Vorname +", bitte wähle zwischen:\nAlle Fahrzeuge anzeigen(1)\nMitarbeiter anlegen(2)\nMitarbeiter ändern(3)")
  Alle_Fahrzeuge_ansehen = input()

  if Alle_Fahrzeuge_ansehen == "1":   # Alle Fahrzeuge ansehen
    Alle_Fahrzeuge_ansehen = []
    FahrzeugeAnzeigen()

  if FahrzeugeAnlegen == "2":         # Mitglied anlegen
    FahrzeugeAnlegen = []
    FahrzeugeAnlegen()
