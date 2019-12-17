# Importe
import mysql
from mysql.connector import cursor, connection
import sys


# Datenbanken Verbindung
def DatenbankenVerbindung():
    # Datenbank MySQL Verbindung
    DB_CBM = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="cbm_Autovermietung"
    )

    #DatenbankenVerbindung()
    # cursor Cursor holen
    cursor = DB_CBM.cursor()

    # cbm_Autovermietung Datenbank anlegen
    cursor.execute("CREATE DATABASE IF NOT EXISTS cbm_Autovermietung")

    # Überprüfen ob Datenbank schon existiert
    cursor.execute("SHOW DATABASES LIKE 'cbm_A%'")
    for x in cursor:
        print("Vorhandene Datenbank", x)

    return DB_CBM
