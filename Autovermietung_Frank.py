"""
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install mysql-connector-python


Quellen
Modul MySQL Connector               -   https://pypi.org/project/mysql-connector-python/
Modul sys                           -   https://docs.python.org/3/library/sys.html
Modul os                            -   https://docs.python.org/3/library/os.html
Foreign Keys                        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze                  -   https://mockaroo.com/
Überprüfung von ein paar Funktionen -   Sven Piehl

"""

# Importe
import mysql
from mysql.connector import cursor, connection
import sys
import os
import time


# Datenbanken Verbindung
def DatenbankenVerbindung():
    try:
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


        DB_CBM = DatenbankenVerbindung()
        cursor = DB_CBM.cursor()
    except:
        print("Der MySQL Server steht momentan nicht zu Verfügung.")

# Datenbank und Tabellen erstellen

# Datenbank Tabelle plz_ip erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS plz_id (plz_id INTEGER PRIMARY KEY AUTO_INCREMENT, plz CHAR(5), ort VARCHAR(50))")

# Datenbank Tabelle mitarbeiter erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS mitarbeiter (mitarbeiter_id INTEGER PRIMARY KEY AUTO_INCREMENT, nachname VARCHAR(50), vorname VARCHAR(50), strasse VARCHAR(50), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(50), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS zweigstelle (zweigstellen_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellenname VARCHAR(50), strasse VARCHAR(50), hausnummer INTEGER, plz_id INTEGER, telefonnr INTEGER, steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen_mitarbeiter erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS zweigstelle_mitarbeiter (zweigstellen_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle kunden erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS kunden (kunden_id INTEGER PRIMARY KEY AUTO_INCREMENT, nachname VARCHAR(50), vorname VARCHAR(50), strasse VARCHAR(50), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(50), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS fahrzeug_preis (fahrzeug_preis_id INTEGER PRIMARY KEY AUTO_INCREMENT, fahrzeug_preis_netto FLOAT)")

# Datenbank Tabelle fahrzeug erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS fahrzeug (fahrzeug_id INTEGER PRIMARY KEY AUTO_INCREMENT, marke VARCHAR(50), klasse VARCHAR(50), status VARCHAR(50), kennzeichen VARCHAR(50), zweigstellen_id INTEGER, fahrzeug_preis_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_preis_id) REFERENCES fahrzeug_preis(fahrzeug_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung (rechnung_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellen_id INTEGER, kunden_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung_details erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung_details (rechnung_id INTEGER, fahrzeug_id INTEGER, verleih_beginn DATE, verleih_ende DATE, FOREIGN KEY (rechnung_id) REFERENCES rechnung(rechnung_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Menüs

def willkommen():
    try:
        choice = input("""
        _______________WILLKOMMEN_______________
        |                 im                   |
        |   Python Projekt - Autovermietung    |
        |   2019 Copyright by. Frank Panzer    |
        |                                      |
        | Es werden alle Funktionen geladen... |
        | Es werden alle Datensätze geladen... |
        |                                      |
        |         Drücken Sie ENTER            |
        |  um alle Funktionen und Datensätze   |
        |  einzuspielen und ins Hauptmenü zu   |
        |  zu gelangen!                        |
        |______________________________________|
         """)
        time.sleep(5)
    except:
        print("Fehler das Willkommen Menü konnte nicht geladen werden.")

# H Menü
def hmenu():
    try:
        choice = input("""
        ____________HAUPTMENUE______________
        |       A: Auflisten               |
        |       B: Anlegen                 |
        |       C: Entfernen               |
        |       D: Bearbeiten              |
        |       E: Kunden Optionen         |
        |----------------------------------|
        |       0: Beenden                 |
        |                                  |
        |__________________©_Frank_Panzer__|

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
    except:
        print("Fehler das Hauptmenü konnte nicht geladen werden.")


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
    try:
        choice = input("""
            _________AUFLISTEN_MENÜ_____________
            |       A: Mitarbeiter auflisten   |
            |       B: Kunden auflisten        |
            |       C: Fahrzeuge auflisten     |
            |       D: Zweigstellen auflisten  |
            |----------------------------------|
            |       1: Hauptmenü               |
            |       0: Beenden                 |
            |                                  |
            |__________________©_Frank_Panzer__|

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
    except:
        print("Fehler das Auflisten Menü konnte nicht geladen werden.")


# Alle Mitglieder anzeigen
def MitarbeiterAuflisten():
    try:
        cursor.execute("SELECT * FROM mitarbeiter")
        records = cursor.fetchall()
        for row in records:
            print(f"Mitarbeiter ID: {row[0]}")
            print(f"Vorname: {row[1]}")
            print(f"Nachname: {row[2]}")
            print(f"Strasse: {row[3]}")
            print(f"Hausnummer: {row[4]}")
            print(f"PLZ ID: {row[5]}")
            print(f"Telefonnummer: {row[6]}")
            print(f"\n")
    except:
        print("Fehler die Mitglieder konnten nicht aufgelistet werden.")

# Alle Kunden anzeigen
def KundenAuflisten():
    try:
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
    except:
        print("Fehler die Kunden konnten nicht aufgelistet werden.")


# Alle Mitglieder anzeigen
def FahrzeugeAuflisten():
    try:
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
    except:
        print("Fehler die Fahrzeuge konnten nicht aufgelistet werden.")


# Alle Zweigstellen anzeigen
def ZweigstellenAuflisten():
    try:
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
    except:
        print("Fehler die Zweigstellen konnten nicht aufgelistet werden.")


# B Menü - Anlegen
def bmenue():
    try:
        choice = input("""
            ___________ANLEGEN_MENÜ_____________
            |       A: Mitarbeiter anlegen     |
            |       B: Kunden anlegen          |
            |       C: Fahrzeuge anlegen       |
            |       D: Zweigstellen anlegen    |
            |       E: Mietpreise anlegen      |
            |----------------------------------|
            |       1: Hauptmenü               |
            |       0: Beenden                 |
            |                                  |
            |__________________©_Frank_Panzer__|

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
            print("Bitte geben Sie A,B,C oder D ein.\nMit 1 Gelangen Sie wieder zurück ins Hauptmenü.\nMit 0(NULL) Beenden Sie das Programm.")
            print("Bitte versuchen Sie es erneut.")
            bmenue()
    except:
        print("Fehler das Anlege Menü konnte nicht erzeugt werden.")



# Abfragen um Mitarbeiter anzulegen
def MitarbeiterAnlegen():
    try:
        print("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
        input_mitarbeiter_nachname = input()
        liste_mitarbeiter=[]
        liste_mitarbeiter.insert(1,input_mitarbeiter_nachname)

        print ("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
        input_mitarbeiter_vorname = input()
        liste_mitarbeiter.insert(2,input_mitarbeiter_vorname)

        print ("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
        input_mitarbeiter_strasse = input()
        liste_mitarbeiter.insert(3,input_mitarbeiter_strasse)

        print ("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
        input_mitarbeiter_hausnummer = input()
        liste_mitarbeiter.insert(4,input_mitarbeiter_hausnummer)

        print ("Bitte geben Sie eien Postleitzahl ein, die Sie hinzufügen wollen: ")
        liste_mitarbeiter_plz=[]
        input_mitarbeiter_postleitzahl = input()
        liste_mitarbeiter_plz.insert(0,input_mitarbeiter_postleitzahl)
        liste_mitarbeiter_vergleich =[]
        liste_mitarbeiter_vergleich.insert(0,input_mitarbeiter_postleitzahl)

        print ("Bitte geben sie den Wohnort des neuen Mitarbeiters ein:")
        input_mitarbeiter_wohnort = input()
        liste_mitarbeiter_plz.insert(1,input_mitarbeiter_wohnort)

        print ("Bitte geben sie die Telefonnummer des neuen Mitarbeiter ein:")
        input_mitarbeiter_telefonnummer = input()
        liste_mitarbeiter.insert(4,input_mitarbeiter_telefonnummer)

        liste_mitarbeiter.append( liste_mitarbeiter_vergleich[0] )
        tupel_mitarbeiter = tuple(liste_mitarbeiter)
        tupel_mitarbeiter_plz = tuple(liste_mitarbeiter_plz)

        cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (?,?)", (tupel_mitarbeiter_plz))
        cursor.execute("INSERT INTO mitarbeiter (nachname, vorname, strasse, hausnummer, telefonnr, plz_id) VALUES (?,?,?,?,?, (SELECT plz_id FROM plz_id WHERE plz = ? limit 1))", tupel_mitarbeiter)
        DB_CBM.commit()
        hmenu()
    except:
        print("Fehler ein Mitglied konnte nicht angelegt werden.")


#########################################################
# Neuer Kunde anlegen
def KundenAnlegen():
    try:
        Kunden_Vorname=input("Bitte gebe den Kunden Vornamen ein denn du anlegen willst: ")
        Kunden_Nachname=input("Bitte gebe den Kunden Nachname ein denn du anlegen willst: ")
        Kunde_Strasse=input("Bitte geben Sie ihre Strasse: ")
        Kunde_Hausnummer=input("Bitte geben sie ihre Hausnummer ein: ")
        Kunde_PLZ=0
        cursor = DB_CBM.cursor()
        while True:
            Kunde_PLZ=input("Bitte geben sie die Postleitzahl ein des Kunden ein: ")
            cursor.execute ("SELECT plz FROM plz_id WHERE plz = %s",(Kunde_PLZ,))
            rows = cursor.fetchall();
            if len( rows ) == 0:
                print(f"Postleitzahl {Kunde_PLZ} ist unbekannt")
                continue;
            break
        tupel=(Kunden_Vorname,Kunden_Nachname,Kunde_Strasse,Kunde_Hausnummer,rows[0][0])
        cursor.execute ("INSERT INTO kunden (nachname,vorname,strasse,hausnummer,plz_id,telefonnr) VALUES (%s,%s,%s,%s,%s,%s)",tupel)
        DB_CBM.commit()
        print("Der Kunde wurde Erfolgreich angelegt.")
        time.sleep(2)
        os.system("cls")
    except mysql.connector.Error as error:
        print("Fehler beim Anlegen eines Kunden. {}".format(error))
#########################################################

# Neue Fahrzeuge einfügen
def FahrzeugeAnlegen():
    try:
        Fahrzeuge_Anlegen1 = input("Bitte geben Sie eine Fahrzeugmarke ein, die Sie hinzufügen wollen: ")
        Fahrzeuge_Anlegen2 = input("Bitte geben Sie eine Fahrzeugmodell ein, die Sie hinzufügen wollen: ")
        Fahrzeuge_Anlegen3 = input("Bitte geben Sie an ob das Auto zu verfügung steht(1) oder Nicht zu verfügung steht(0): ")

        cursor = DB_CBM.cursor()

        # ID für Fahrzeug wird gehollt
        res = cursor.execute("INSERT INTO fahrzeuge (fahrzeug_id) VALUES (%s)", (Fahrzeuge_Anlegen,))
        print(res.lastinsertid)
        fzid = res.lastinsertid

        cursor.execute("UPDATE fahrzeuge SET (fahrzeug_id) WHERE fahrzeug_id =" + fzid, )
        cursor.execute("UPDATE fahrzeuge SET (marke) VALUES (%s)", (Fahrzeuge_Anlegen1,))
        cursor.execute("UPDATE fahrzeuge SET (modell) VALUES (%s)", (Fahrzeuge_Anlegen2,))
        cursor.execute("UPDATE fahrzeuge SET (status) VALUES (%s)", (Fahrzeuge_Anlegen3,))
        cursor.execute("UPDATE fahrzeuge SET (kennzeichen) VALUES (%s)", (Fahrzeuge_Anlegen1,))
        cursor.execute("UPDATE fahrzeuge SET (zweigstelle_id) VALUES (%s)", (Fahrzeuge_Anlegen2,))
        cursor.execute("UPDATE fahrzeuge SET (fahrzeug_preis_id) VALUES (%s)", (Fahrzeuge_Anlegen3,))

        myresult = cursor.fetchall()

        for x in myresult:
            print("Das sind alle Fahrzeuge: ", x)
    except:
        print("Fehler beim Fahrzeug anlegen.")

def ZweigstellenAnlegen():
    try:
        dmenue()
    except:
        print("Das Hauptmenü konnte nicht geöffnet werden.")


# C Menü - Entfernen
def cmenue():
    try:
        choice = input("""
            ___________ENTFERNEN_MENUE__________
            |       A: Mitglieder entfernen    |
            |       B: Kunden entfernen        |
            |       C: Fahrzeuge entfernen     |
            |       D: Zweigstellen entfernen  |
            |----------------------------------|
            |       1: Hauptmenü               |
            |       0: Beenden                 |
            |                                  |
            |__________________©_Frank_Panzer__|

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
    except:
        print("Fehler das Entfernen Menü konnte nicht aufgelistet werden.")

def MitgliederEntfernen():
    try:
        pass
    except:
        print("Fehler ein Mitglied konnte nicht entfernt werden.")


def KundenEntfernen():
    try:
        os.system("cls")
        cursor = DB_CBM.cursor()
        cursor.execute("SELECT * FROM kunden")
        result = cursor.fetchall()
        for i in result:
            print(f"Kunden ID: {i[0]:<10}  Vorname: {i[2]:<10}  Nachname: {i[1]:<10}  Straße: {i[3]:<10}  Hausnummer: {i[4]:<10}  Postleitzahl: {i[5]:<10} Telefonnummer: {i[6]:<10}")
            print("Liste der Kunden.")
            LoeschenUeberKundenID = input("Bitte Kunden ID des Kundes was Gelöscht werden soll: ")
            cursor = DB_CBM.cursor()
            klass = (LoeschenUeberKundenID,)
            cursor.execute("DELETE FROM kunden WHERE kunden_id = (%s)",(LoeschenUeberKundenID,))
            DB_CBM.commit()
            print("Der Kunde wurde erfolgreich entfernt.")
        time.sleep(2)
        os.system("cls")
    except:
        print("Fehler ein Kunde konnte nicht entfernt werden.")



def FahrzeugeEntfernen():
    try:
        pass
    except:
        print("Fehler ein Fahrzeug konnte nicht entfernt werden.")


def ZweigstellenEntfernen():
    try:
        pass
    except:
        print("Fehler eine Zweigstelle konnte nicht entfernt werden.")


# D Menü Bearbeiten
def dmenue():
    try:
        choice = input("""
            _________BEARBEITEN_MENUE___________
            |       A: Mitarbeiter bearbeiten  |
            |       B: Kunden bearbeiten       |
            |       C: Fahrzeuge bearbeiten    |
            |       D: Mitpreise bearbeiten    |
            |----------------------------------|
            |       1: Hauptmenü               |
            |       0: Beenden                 |
            |                                  |
            |__________________©_Frank_Panzer__|

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
    except:
        print("Fehler das bearbeiten Menü konnte nicht geladen werden.")


def MitarbeiterBearbeiten():
    try:
        pass
    except:
        print("Fehler ein Mitglied konnte nicht bearbeitet werden.")


def KundenBearbeiten():
    try:
        pass
    except:
        print("Fehler ein Kunde konnte nicht bearbeitet werden.")


def FahrzeugeBearbeiten():
    try:
        pass
    except:
        print("Fehler ein Fahrzeug konnte nicht bearbeitet werden.")


def MitpreiseBearbeiten():
    try:
        os.system("cls")
        cursor = DB_CBM.cursor()
        Mitpreis_input=print("Bitte gebe die ID vom Fahrzeug ein welches du bearbeiten willst: ")
        Mitpreis_input=()
        cursor.execute("UPDATE fahrzeug_preis SET fahrzeug_preis_netto = "+ {Mitpreis_input} +" WHERE fahrzeug_preis.fahrzeug_preis_id = 1;")
        result = cursor.fetchall()

    except:
        print("Fehler ein Mietpreis konnte nicht bearbeitet werden.")


# E Menü - Kunden Optionen
def emenue():
    try:
        choice = input("""
            _________KUNDEN_OPTIONEN___________________
            |       A: Fahrzeug Ausleihen              |
            |       B: Fahrzeug Zurückgeben            |
            |       C: Fahrzeug sotieren nach Status   |
            |       D: Fahrzeug sotieren nach Modell   |
            |------------------------------------------|
            |       1: Hauptmenü                       |
            |       0: Beenden                         |
            |                                          |
            |__________________________©_Frank_Panzer__|

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
    except:
        print("Fehler das Kunden Optionen Menü konnte nicht geladen werder.")


def FahrzeugAusleihen():
    try:
        pass
    except:
        print("Fehler ein Fahrzeug konnte nicht aufgeliehen werden.")


def FahrzeugZurueckgeben():
    try:
        pass
    except:
        print("Fehler ein Fahrzeug konnte nicht zurückgegeben werden.")


def FahrzeugSotierenStatus():
    try:
        cursor.execute("SELECT * FROM fahrzeug ORDER BY fahrzeug.status DESC")
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
    except:
        print("Fehler die Fahrzeuge konnten nicht nach dem Status sotiert werden.")


def FahrzeugSotierenModell():
    try:
        cursor.execute("SELECT * FROM fahrzeug ORDER BY fahrzeug.marke DESC")
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
    except:
        print("Fehler die Fahrzeuge konnten nicht nach dem Modell sotiert werden.")


willkommen()
hmenu()
