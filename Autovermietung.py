'''
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

Quellen
Menü              -   http://effbot.org/tkinterbook/menu.htm
MySQL Connector   -   https://pypi.org/project/mysql-connector-python/
Foreign Keys      -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html


'''
# Importe
import mysql
import mysql.connector
from tkinter import *
import time
import sys

# Datenbank MySQL Verbindung
DB_CBM = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "cbm_Autovermietung"
)

# mycursor Cursor holen
mycursor = DB_CBM.cursor()

# cbm_Autovermietung Datenbank anlegen
mycursor.execute("CREATE DATABASE IF NOT EXISTS cbm_Autovermietung")

# Überprüfen ob Datenbank schon existiert
mycursor.execute("SHOW DATABASES LIKE 'cbm_A%'")
for x in mycursor:
  print("Vorhandene Datenbank",x)

# Datenbank Tabelle plz_ip erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS plz_id ( plz_id INT PRIMARY KEY AUTO_INCREMENT, plz VARCHAR(5) DEFAULT NULL, ort VARCHAR(50) DEFAULT NULL )")

# Datenbank Tabelle mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS mitarbeiter(mitarbeiter_id INTEGER PRIMARY KEY AUTO_INCREMENT,vorname VARCHAR(50),nachname VARCHAR(50),strasse VARCHAR(80),hausnummer INTEGER,plz_id INTEGER,telefonnr VARCHAR(50),FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstelle (zweigstellen_id INTEGER PRIMARY KEY AUTO_INCREMENT, strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr INTEGER, steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen_mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstellen_mitarbeiter (zweigstellen_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle kunden erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (kunden_id INTEGER PRIMARY KEY AUTO_INCREMENT, nachname VARCHAR(50), vorname VARCHAR(30), strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(80), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug_preis (fahrzeug_preis_id INTEGER PRIMARY KEY AUTO_INCREMENT, fahrzeug_id INTEGER, fahrzeug_preis_netto FLOAT)")

# Datenbank Tabelle fahrzeug erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug (fahrzeug_id INTEGER PRIMARY KEY AUTO_INCREMENT, marke VARCHAR(50), modell VARCHAR(50), status VARCHAR(30), kennzeichen VARCHAR(20), zweigstellen_id INTEGER, fahrzeug_preis_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_preis_id) REFERENCES fahrzeug_preis(fahrzeug_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis Fremdschlüssel erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug_preis (FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS rechnung (rechnung_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellen_id INTEGER, kunden_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung_details erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS rechnung_details (rechnung_id INTEGER, fahrzeug_id INTEGER, verleih_beginn DATE, verleih_ende DATE, FOREIGN KEY (rechnung_id) REFERENCES rechnung(rechnung_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")


# Beginn der Funktionen

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
