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
def ZweigstellenAuflisten():
    cursor.execute("SELECT * FROM zweigstelle ")
    result = cursor.fetchall()
    for row in result:
        print(f"zweigstellen_id: {row[0]:5} zweigstellen Strasse: {row[1]:10}  ")

ZweigstellenAuflisten()