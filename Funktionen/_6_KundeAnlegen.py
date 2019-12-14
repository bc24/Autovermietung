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
# Neuer Kunde anlegen
from mysql.connector import connection, cursor

Vorname=input("Bitte gebe den Kunden Vornamen ein denn du anlegen willst: ")
Nachname=input("Bitte gebe den Kunden Nachname ein denn du anlegen willst: ")
def KundeAnlegen():
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
    connection.commit()