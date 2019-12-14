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

import Funktionen.Datenbanken

# Übersicht über die vorhandenen Fahrzeuge

def FahrzeugeAnzeigen():
  mycursor = DB_CBM.cursor()
  mycursor.execute("SELECT * FROM fahrzeuge")
  myresult = mycursor.fetchall()
  print("SELECT * FROM fahrzeuge")
