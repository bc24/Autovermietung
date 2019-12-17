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
def ZweigstellenAuflisten(conn, cursor):
    cursor.execute("SELECT * FROM zweigstelle")
    records = cursor.fetchall()
    for row in records:
        print(f"Zweigstellen ID: {row[0]}")
        print(f"Strasse: {row[1]}")
        print(f"Hausnummer: {row[2]}")
        print(f"PLZ ID: {row[3]}")
        print(f"Telefonnr: {row[4]}")
        print(f"Steuernummer ID: {row[5]}")
        print(f"\n")
