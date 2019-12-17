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
# Imports
from mysql.connector import cursor


# Alle Kunden anzeigen
def KundenAnzeigen(conn, cursor):
    cursor.execute("SELECT * FROM kunden ")
    records = cursor.fetchall()
    for row in records:
        print(f"Kunden ID: {row[0]}")
        print(f"Vorname: {row[2]}")
        print(f"Nachname: {row[1]}")
        print(f"Strasse: {row[3]}")
        print(f"Hausnummer: {row[4]}")
        print(f"PLZ ID: {row[5]}")
        print(f"Telefonnummer: {row[6]}")
        print(f"\n")
