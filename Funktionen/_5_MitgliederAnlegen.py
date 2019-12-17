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

def MitgliederAnlegen(conn, cursor):
    cursor.execute(INSERT INTO mitarbeiter (vorname,nachname,strasse,hausnummer,plz_id,telefonnr) VALUES (%s,%s,%s,%s,%s,%s))
# ID für Mitglieder wird gehollt
    res = cursor.execute("INSERT INTO mitglieder (mitglieder_id) VALUES (%s,%s,%s,%s,%s,%s)", (MitgliederAnlegen,))
    print(res.lastinsertid)
    mgid = res.lastinsertid

# Abfragen um Mitarbeiter anzulegen
    Mitglied_Vorname = input("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
    Mitglied_Nachname = input("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
    Mitglied_Strasse = input("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
    Mitglied_Hausnummer = input("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
    Mitglied_Telefonnummer = input("Bitte geben Sie eien Telefonnummer ein, die Sie hinzufügen wollen: ")
    Mitglied_PLZ = input("Bitte geben Sie die PLZ ein, die Sie hinzufügen wollen: ")

# Den Cursor holen und in einer Tupel übergeben
    cursor = cursor.cursor()

    cursor.execute("UPDATE mitglieder SET plz_id=(SELECT plz_id FROM plz_id WHERE plz=? limit 1) WHERE mitglieder_id = ?", (Mitglied_PLZ, mgid))
    cursor.execute("INSERT INTO mitglieder vorname=? WHERE mitglieder_id = ? ", (Mitglied_Vorname, mgid))
    cursor.execute("UPDATE mitglieder SET nachname=? WHERE vorname = ? ", (Mitglied_Nachname, mgid))
    cursor.execute("UPDATE mitglieder SET strasse=? WHERE nachname = ? ", (Mitglied_Strasse, mgid))
    cursor.execute("UPDATE mitglieder SET hausnummer=? WHERE strasse = ? ", (Mitglied_Hausnummer, mgid))
    cursor.execute("UPDATE mitglieder SET telefonnr=? WHERE hausnummer = ? ", (Mitglied_Telefonnummer, mgid))


    result = cursor.fetchall()
    cursor.commit()
