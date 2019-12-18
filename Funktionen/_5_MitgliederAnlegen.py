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
# Datenbank und Tabellen erstellen


DB_CBM = DatenbankenVerbindung()
cursor = DB_CBM.cursor()

'''
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

    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (?,?)", (tupel_mitarbeiter_plz))
    cursor.execute("INSERT INTO mitarbeiter (nachname, vorname, strasse, hausnummer, telefonnr, plz_id) VALUES (?,?,?,?,?, (SELECT plz_id FROM plz_id WHERE plz = ? limit 1))", tupel_mitarbeiter)
    DB_CBM.commit(conn, cursor)
    hmenu()
'''
###################### Alte Def
def MitgliederAnlegen(conn, cursor):
    print("Bitte geben Sie den Nachnamen des neuen Mitarbeiters ein:")
    user_input_m_nachname = input()
    liste_mitarbeiter=[]
    liste_mitarbeiter.insert(0,user_input_m_nachname)
    print ("Bitte geben sie den Vornamen des Mitarbeiters ein:")
    user_input_m_vorname = input()
    liste_mitarbeiter.insert(1,user_input_m_vorname)
    print ("Bitte geben sie die Strasse des neuen Mitarbeiters ein:")
    user_input_m_strasse = input()
    liste_mitarbeiter.insert(2,user_input_m_strasse)
    print ("Bitte geben sie die Hausnummer des neuen Mitarbeiters ein:")
    user_input_m_hausnummer = input()
    liste_mitarbeiter.insert(3,user_input_m_hausnummer)
    print ("Bitte geben sie die Postleitzahl des neuen Mitarbeiters ein:")
    liste_mitarbeiter_plz=[]
    user_input_m_postleitzahl = input()
    liste_mitarbeiter_plz.insert(0,user_input_m_postleitzahl)
    liste_ma_vergleich =[]
    liste_ma_vergleich.insert(0,user_input_m_postleitzahl)
    print ("Bitte geben sie den Wohnort des neuen Mitarbeiters ein:")
    user_input_m_wohnort = input()
    liste_mitarbeiter_plz.insert(1,user_input_m_wohnort)
    print ("Bitte geben sie die Telefonnummer des neuen Mitarbeiter ein:")
    user_input_m_telefonnummer = input()
    print("Danke für ihre Eingabe")
    liste_mitarbeiter.insert(4,user_input_m_telefonnummer)
    liste_mitarbeiter.append( liste_ma_vergleich[0] )
    tupel_mitarbeiter = tuple(liste_mitarbeiter)
    tupel_mitarbeiter_plz = tuple(liste_mitarbeiter_plz)
    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (?,?)", (tupel_mitarbeiter_plz))
    cursor.execute("INSERT INTO mitarbeiter (nachname, vorname, strasse, hausnummer, telefonnr, plz_id) VALUES (?,?,?,?,?, (SELECT plz_id FROM plz_id WHERE plz = ? limit 1))", tupel_mitarbeiter)
    DB_CBM.commit()
    hmenu()