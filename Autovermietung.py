'''
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

Quellen
Menü                -   http://effbot.org/tkinterbook/menu.htm
MySQL Connector     -   https://pypi.org/project/mysql-connector-python/
Foreign Keys        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze  -   https://mockaroo.com/


'''

# Importe

# Datenbank MySQL Verbindung

# Beginn der Funktionen

# Übersicht über die vorhandenen Fahrzeuge
# Hauptmenue


# Übersicht über die vorhandenen Fahrzeuge
# Menüpunkt 1

# Neue Fahrzeuge einfügen
# Menüpunkt 2

# Neue Fahrzeuge entfernen
# Menüpunkt 3

# Fahrzeuge bearbeiten
# Menüpunkt 4

# Mietpreise für Fahrzeuge festlegen
# Menüpunkt 5

# Sortierung der Fahrzeuge
# Menüpunkt 6

# Fahrzeug Modell
# Menüpunkt 7

# Fahrzeug Status
# Menüpunkt 8

# Fahrzeug Vorhanden
# Menüpunkt 9

# Fahrzeug Verliehen
# Menüpunkt 10

# Alle Mitarbeiter anzeigen
# Menüpunkt 11

# Mitarbeiter anlegen
# Menüpunkt 12

# Mitglieder Ändern
# Menüpunkt 13

# Alle Kundne anzeigen
# Menüpunkt 14

# Neuer Kunde anlegen
# Menüpunkt 15

# Neue Kunde ändernn
# Menüpunkt 16

# Fahrzeug leihen
# Menüpunkt 17

# Fahrzeug zurückbringen
# Menüpunkt 18

# Fahrzeug zustand Fahrzeug beschädigt/zerstört
# Menüpunkt 19


# Consolen Abfragen
# Abfrage kunde oder Mitarbeiter
from Funktionen.MitgliederAendern_13 import MitgliederAendern
from mysql.connector import cursor, connection
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
        plz = input()
        liste_kunde_plz = []
        liste_kunde_plz.insert(1, plz)
        print("Bitte geben Sie ihren Wohnort ein:")
        Ort = input()
        liste_kunde_plz.insert(2, Ort)
        print("Bitte geben sie ihre Telefonnummer im Format 0421123456 (Also ohne Lehrzeichen,+ oder -)")
        Telefon = input()
        liste_kunde.insert(4, Telefon)

        # Trupel übergeben
        tupel_kunde = (liste_kunde)
        tupel_kunde_plz = (liste_kunde_plz)

        # Übergabe der eingegebenen Datensätze in die Datenbank Tabelle
        cursor.execute(
            "INSERT INTO kunden (nachname, vorname, strasse, hausnummer, telefonnr) VALUES (?,?,?,?,?), (tupel_kunde)")
        cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (?,?), (tupel_kunde_plz)")

        # Übertragen der Datensätze
        # noinspection PyUnresolvedReferences
        connection.commit()

        print("Sie haben folgende Daten eingegeben. Bitte merken sie sich ihre Kundennummer!")
        sql = "SELECT * FROM kunden"
        print(sql)

    if Frage1 == "2":
        mitglieder = []
        print("Bitte geben sie ihre Kundennummer ein:")

### Wenn Mitarbeiter dann
if Frage1 == "2":
    print("Willkommen zurück Herr/Frau", Nachname + "!")
    print("Hallo",
          Vorname + ", bitte wähle zwischen:\nAlle Mitglieder anzeigen(1)\nMitarbeiter anlegen(2)\nMitarbeiter ändern(3)")
    Alle_Mitglieder_ansehen = input()

    # Alle Mitglieder ansehen
    if Alle_Mitglieder_ansehen == "1":
        Alle_Mitglieder_ansehen = []
        Alle_Mitglieder_ansehen()

    # Mitglied anlegen
    if Mitglieder_Anlegen == "2":
        Mitglieder_Anlegen = []
        MitgliederAnlegen()

    # Mitglied ändern
    if Mitglieder_Aendern == "3":
        Mitglieder_Aendern = []
        MitgliederAendern()
