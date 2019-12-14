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

    DatenbankenVerbindung()
    # mycursor Cursor holen
    mycursor = DB_CBM.cursor()

    # cbm_Autovermietung Datenbank anlegen
    mycursor.execute("CREATE DATABASE IF NOT EXISTS cbm_Autovermietung")

    # Überprüfen ob Datenbank schon existiert
    mycursor.execute("SHOW DATABASES LIKE 'cbm_A%'")
    for x in mycursor:
        print("Vorhandene Datenbank", x)


# Datenbank und Tabellen erstellen

# Datenbank Tabelle plz_ip erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS plz_id ( plz_id INT PRIMARY KEY AUTO_INCREMENT, plz VARCHAR(5) DEFAULT NULL, ort VARCHAR(50) DEFAULT NULL )")

# Datenbank Tabelle mitarbeiter erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS mitarbeiter(mitarbeiter_id INTEGER PRIMARY KEY AUTO_INCREMENT,vorname VARCHAR(50),nachname VARCHAR(50),strasse VARCHAR(80),hausnummer INTEGER,plz_id INTEGER,telefonnr VARCHAR(50),FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS zweigstelle (zweigstellen_id INTEGER PRIMARY KEY AUTO_INCREMENT, strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr INTEGER, steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen_mitarbeiter erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS zweigstellen_mitarbeiter (zweigstellen_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle kunden erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS kunden (kunden_id INTEGER PRIMARY KEY AUTO_INCREMENT, nachname VARCHAR(50), vorname VARCHAR(30), strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(80), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS fahrzeug_preis (fahrzeug_preis_id INTEGER PRIMARY KEY AUTO_INCREMENT, fahrzeug_id INTEGER, fahrzeug_preis_netto FLOAT)")

# Datenbank Tabelle fahrzeug erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS fahrzeug (fahrzeug_id INTEGER PRIMARY KEY AUTO_INCREMENT, marke VARCHAR(50), modell VARCHAR(50), status VARCHAR(30), kennzeichen VARCHAR(20), zweigstellen_id INTEGER, fahrzeug_preis_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_preis_id) REFERENCES fahrzeug_preis(fahrzeug_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis Fremdschlüssel erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS fahrzeug_preis (FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung (rechnung_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellen_id INTEGER, kunden_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung_details erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung_details (rechnung_id INTEGER, fahrzeug_id INTEGER, verleih_beginn DATE, verleih_ende DATE, FOREIGN KEY (rechnung_id) REFERENCES rechnung(rechnung_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")


# Menüs

def willkommen():
    choice = input("""
    _______________WILLKOMMEN_______________
    |                 im                   |
    |    Python Projekt Autovermietung     |
    |   2019 Copyright by. Frank Panzer    |
    |                                      |
    | Es werden alle Funktionen geladen... |
    |                                      |
    |         Drücken Sie ENTER            |
    |    um ins Hauptmenü zu gelangen.     |
    |______________________________________|
     """)


# H Menü
def hmenu():
    choice = input("""
    ____________HAUPTMENUE______________
    |       A: Auflisten               |
    |       B: Anlegen                 |
    |       C: Entfernen               |
    |       D: Bearbeiten              |
    |       E: Kunden Optionen         |
    |----------------------------------|       
    |       0: Beenden                 |
    |__________________________________|

    Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        Auflisten()
    elif choice == "B" or choice == "b":
        Anlegen()
    elif choice == "C" or choice == "c":
        Entfernen()
    elif choice == "D" or choice == "d":
        Bearbeiten()
    elif choice == "E" or choice == "e":
        KundenOptionen()
    elif choice == "0" or choice == "null":
        sys.exit()
    else:
        print("Bitte geben Sie A,B,C,D oder E ein. Mit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        hmenu()


def Auflisten():
    amenue()


def Anlegen():
    bmenue()


def Entfernen():
    cmenue()


def Bearbeiten():
    dmenue()


def KundenOptionen():
    emenue()


# A Menü - Auflisten
def amenue():
    choice = input("""
        _________AUFLISTEN_MENÜ_____________
        |       A: Mitarbeiter auflisten   |
        |       B: Kunden auflisten        |
        |       C: Fahrzeuge auflisten     |
        |       D: Zweigstellen auflisten  |
        |----------------------------------|
        |       1: Hauptmenü               |      
        |       0: Beenden                 |
        |__________________________________|

        Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        MitarbeiterAuflisten()
    elif choice == "B" or choice == "b":
        KundenAuflisten()
    elif choice == "C" or choice == "c":
        FahrzeugeAuflisten()
    elif choice == "D" or choice == "d":
        ZweigstellenAuflisten()
    elif choice == "1" or choice == "eins":
        hmenu()
    elif choice == "0" or choice == "0":
        sys.exit()
    else:
        print(
            "Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        amenue()


def MitarbeiterAuflisten():
    import Funktionen._1_Mitglieder_ansehen


def KundenAuflisten():
    import Funktionen._2_KundenAnzeigen


def FahrzeugeAuflisten():
    import Funktionen._3_FahrzeugeAnzeigen


def ZweigstellenAuflisten():
    import Funktionen._4_ZweigstellenAuflisten


# B Menü - Anlegen
def bmenue():
    choice = input("""
        ___________ANLEGEN_MENÜ_____________
        |       A: Mitarbeiter anlegen     |
        |       B: Kunden anlegen          |
        |       C: Fahrzeuge anlegen       |
        |       D: Zweigstellen anlegen    |
        |       E: Mietpreise anlegen      |
        |----------------------------------|
        |       1: Hauptmenü       
        |       0: Beenden                 |
        |__________________________________|

        Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        MitarbeiterAnlegen()
    elif choice == "B" or choice == "b":
        KundenAnlegen()
    elif choice == "C" or choice == "c":
        FahrzeugeAnlegen()
    elif choice == "D" or choice == "d":
        ZweigstellenAnlegen()
    elif choice == "1" or choice == "eins":
        hmenu()
    elif choice == "0" or choice == "0":
        sys.exit()
    else:
        print(
            "Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        bmenue()


def MitarbeiterAnlegen():
    import Funktionen._5_MitgliederAnlegen


def KundenAnlegen():
    import Funktionen._6_KundeAnlegen


def FahrzeugeAnlegen():
    import Funktionen._7_FahrzeugeAnlegen


def ZweigstellenAnlegen():
    dmenue()


# C Menü - Entfernen
def cmenue():
    choice = input("""
        ___________ENTFERNEN_MENUE__________
        |       A: Mitglieder entfernen    |
        |       B: Kunden entfernen        |
        |       C: Fahrzeuge entfernen     |
        |       D: Zweigstellen entfernen  |
        |----------------------------------|
        |       1: Hauptmenü               |      
        |       0: Beenden                 |
        |__________________________________|

        Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        MitgliederEntfernen()
    elif choice == "B" or choice == "b":
        KundenEntfernen()
    elif choice == "C" or choice == "c":
        FahrzeugeEntfernen()
    elif choice == "D" or choice == "d":
        ZweigstellenEntfernen()
    elif choice == "1" or choice == "eins":
        hmenu()
    elif choice == "0" or choice == "0":
        sys.exit()
    else:
        print(
            "Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        cmenue()


def MitgliederEntfernen():
    import Funktionen._8_MitgliederEntfernen


def KundenEntfernen():
    import Funktionen._9_KundenEntfernen


def FahrzeugeEntfernen():
    import Funktionen._10_FahrzeugeEntfernen


def ZweigstellenEntfernen():
    import Funktionen._11_ZweigstellenEntfernen


# D Menü Bearbeiten
def dmenue():
    choice = input("""
        _________BEARBEITEN_MENUE___________
        |       A: Mitarbeiter bearbeiten  |
        |       B: Kunden bearbeiten       |
        |       C: Fahrzeuge bearbeiten    |
        |       D: Mitpreise bearbeiten    |
        |----------------------------------|
        |       1: Hauptmenü               |      
        |       0: Beenden                 |
        |__________________________________|

        Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        MitarbeiterBearbeiten()
    elif choice == "B" or choice == "b":
        KundenBearbeiten()
    elif choice == "C" or choice == "c":
        FahrzeugeBearbeiten()
    elif choice == "D" or choice == "d":
        MitpreiseBearbeiten()
    elif choice == "1" or choice == "eins":
        hmenu()
    elif choice == "0" or choice == "0":
        sys.exit()
    else:
        print(
            "Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        dmenue()


def MitarbeiterBearbeiten():
    import Funktionen._12_MitgliederAendern


def KundenBearbeiten():
    import Funktionen._13_KundeAendern


def FahrzeugeBearbeiten():
    import Funktionen._14_FahrzeugeBearbeiten


def MitpreiseBearbeiten():
    import Funktionen._15_MitpreiseBearbeiten


# E Menü - Kunden Optionen
def emenue():
    choice = input("""
        _________KUNDEN_OPTIONEN___________________
        |       A: Fahrzeug Ausleihen              |
        |       B: Fahrzeug Zurückgeben            |
        |       C: Fahrzeug sotieren nach Status   |
        |       D: Fahrzeug sotieren nach Modell   |
        |------------------------------------------|
        |       1: Hauptmenü                       |      
        |       0: Beenden                         |
        |__________________________________________|

        Bitte treffe eine Wahl: """)

    if choice == "A" or choice == "a":
        FahrzeugAusleihen()
    elif choice == "B" or choice == "b":
        FahrzeugZurueckgeben()
    elif choice == "C" or choice == "c":
        FahrzeugSotierenStatus()
    elif choice == "D" or choice == "d":
        FahrzeugSotierenModell()
    elif choice == "1" or choice == "eins":
        hmenu()
    elif choice == "0" or choice == "0":
        sys.exit()
    else:
        print(
            "Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
        print("Bitte versuchen Sie es erneut.")
        emenue()


def FahrzeugAusleihen():
    import Funktionen._16_FahrzeugAusleihen


def FahrzeugZurueckgeben():
    import Funktionen._17_FahrzeugZurueckgeben


def FahrzeugSotierenStatus():
    import Funktionen._18_FahrzeugSotierenStatus


def FahrzeugSotierenModell():
    import Funktionen._19_FahrzeugSotierenModell


willkommen()
hmenu()
