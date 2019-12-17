"""
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install mysql-connector-python


Quellen
Easy Menü                           -   https://pypi.org/project/easy-menu/
MySQL Connector                     -   https://pypi.org/project/mysql-connector-python/
Foreign Keys                        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze                  -   https://mockaroo.com/
Überprüfung von ein paar Funktionen -   Sven Piehl

"""

# Imports
from mysql.connector import cursor


# Alle Mitglieder anzeigen
def FahrzeugeAnzeigen(conn, cursor):
    cursor.execute("SELECT * FROM fahrzeug")
    records = cursor.fetchall()
    for row in records:
        print(f"Fahrzeug ID: {row[0]}")
        print(f"Marke: {row[1]}")
        print(f"Modell: {row[2]}")
        print(f"Status: {row[3]}")
        print(f"Kennzeichen: {row[4]}")
        print(f"Zweigstellen ID: {row[5]}")
        print(f"Fahrzeug Preis ID: {row[6]}")
        print(f"\n")
