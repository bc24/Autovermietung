"""
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install mysql-connector-python


Quellen
MySQL Connector                     -   https://pypi.org/project/mysql-connector-python/
Foreign Keys                        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze                  -   https://mockaroo.com/
Überprüfung von ein paar Funktionen -   Sven Piehl

"""

# Datenbanken Verbindung
from mysql.connector import cursor

# Abfragen um Mitarbeiter anzulegen
def MitgliederAnlegen(conn, cursor):

    Mitglied_Vorname = input("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter=[]
    liste_mitarbeiter.insert(0,Mitglied_Vorname)

    Mitglied_Nachname = input("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter.insert(1,Mitglied_Nachname)

    Mitglied_Strasse = input("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter.insert(2,Mitglied_Strasse)

    Mitglied_Hausnummer = input("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter.insert(3,Mitglied_Hausnummer)

    Mitglied_Telefonnummer = input("Bitte geben Sie eien Telefonnummer ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter.insert(4,Mitglied_Telefonnummer)

    Mitglied_PLZ = input("Bitte geben Sie die PLZ ein, die Sie hinzufügen wollen: ")
    liste_plz=[]
    liste_plz.insert(0,Mitglied_PLZ)
    liste_vergleich=[]
    liste_vergleich.insert(0,Mitglied_PLZ)

    Mitglied_Wohnort = input("Bitte geben Sie eien Wohnort ein, die Sie hinzufügen wollen: ")
    Mitglied_PLZ.insert(1,Mitglied_Wohnort)

    liste_mitarbeiter.insert(liste_vergleich[0])
    tuple_mitarbeiter = tuple(liste_mitarbeiter)
    tuple_mitarbeiter_plz = tuple(liste_plz)

    cursor.execute(INSERT INTO plz_id(plz,ort) VALUES (?,?),(tuple_mitarbeiter_plz))
    cursor.execute(INSERT INTO mitarbeiter(vorname,nachname,strasse,hausnummer,telefonnr,plz_id) VALUES (?,?,?,?,?, (SELECT plz_id FROM plz_id WHERE plz = ? limit 1)),tuple_mitarbeiter)
    DB_CBM.commit(conn, cursor)
    hmenu()
