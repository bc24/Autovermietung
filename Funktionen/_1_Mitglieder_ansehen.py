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


# Alle Mitglieder anzeigen
def Mitglieder_ansehen():
    cursor.execute("SELECT * FROM mitglieder ")
    result = cursor.fetchall()
    for row in result:
        print(f"Mitarbeiter ID: {row[0]:5} Vorname: {row[1]:10} Nachname: {row[2]:15} ")


Mitglieder_ansehen()
