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
from typing import Tuple
import mysql
from mysql.connector import cursor, connection
import sys
import os
import time


# Datenbanken Verbindung
def DatenbankenVerbindung():
    # Datenbank MySQL Verbindung
    DB_CBM = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="cbm_Autovermietung"
    )

    # DatenbankenVerbindung()
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

# Datenbank Tabelle ausgeliehen_details erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS ausgeliehen_details (ausgeliehen_id INTEGER PRIMARY KEY AUTO_INCREMENT, kunden_id INTEGER, verleih_anfang DATE, verleih_ende DATE, fahrzeug_id INTEGER, status VARCHAR(50), FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung (rechnung_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellen_id INTEGER, kunden_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung_details erstellen
cursor.execute(
    "CREATE TABLE IF NOT EXISTS rechnung_details (rechnung_id INTEGER, fahrzeug_id INTEGER, verleih_beginn DATE, verleih_ende DATE, FOREIGN KEY (rechnung_id) REFERENCES rechnung(rechnung_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Dummy Datensätze erstellen
"""
# plz_id
cursor.execute("INSERT INTO plz_id (plz_id, plz, ort) VALUES(1, 28201, Bremen),(2, 28777, Bremen),(3, 28199, Xinheng),(4, 28199, Ogaminan),(5, 1219, Mancilang),(6, 22151, Hamburg),(7, 35334, Arcachon),(8, 4888, Plaza de Caisán),(9, 66815, Sut-Khol’),(10, 49800, Butajīra),(11, 28757, Savran’),(12, 28199, Huangfang),(13, 78967, Buritis),(14, 79783, San Rafael),(15, 28199, Mafang),(16, 28755, Hengliang),(17, 43605, Karlovo),(18, 94631, Rungis),(19, 27201, Hanting),(20, 28259, Muli),(21, 28745, Mashizhai),(22, 28946, Caicara),(23, 37347, Rudolfov),(24, 78430, Rancho Nuevo),(25, 63441, Sandayong Sur),(26, 28201, Gananoque),(27, 28201, Xingong),(28, 28201, Awarawar),(29, 28201, Krajan Kerjo),(30, 28201, Chaoyang),(31, 36372, Kizlyar),(32, 29201, Coaldale),(33, 46205, Linhares),(34, 28201, Dongping),(35, 28201, Nouvelle France),(36, 28201, Vom),(37, 28201, Talā),(38, 67502, Blagoveshchensk),(39, 41355, Vineuil),(40, 28201, Xiangyanglu),(41, 28201, Bihać),(42, 13155, Otlja),(43, 28201, Socos),(44, 13075, Haligue),(45, 9025, Digkilaan),(46, 64922, Shebalino),(47, 7165, Villa Gesell),(48, 28201, Baalbek),(49, 28201, Teongtoda),(50, 28201, Taokeng)")

# mitarbeiter
cursor.execute("INSERT INTO mitarbeiter (mitarbeiter_id, nachname, vorname, strasse, hausnummer, plz_id, telefonnr) VALUES(1, Koubek, Neill, Summit, 196, NULL, 3898283207),(2, Demageard, Richmound, Ramsey, 6266, NULL, 7932862027),(3, Connal, Clementius, Riverside, 931, NULL, 2161213283),(6, Gooble, Nettle, Tomscot, 8343, NULL, 4349354479),(8, Dunsford, Daisey, Linden, 5, NULL, 9667978058),(10, Haslen, Noak, Darwin, 49340, NULL, 9192232298),(12, Cowope, Nady, Garrison, 6954, NULL, 3926851771),(17, Chaimson,Eran, Sutherland, 1232, NULL, 9437504005),(18, Gopsall, Zola, Sachs, 522, NULL, 8094667188),(20, McAuley, Ashia, 1st, 4614, NULL, 1842697287),(21, Isaacs, Georas, Dunning, 4, NULL, 5262047822),(22, Savory, Theresa, Cottonwood, 26, NULL, 3846647756),(23, Arnau, Moses, Gina, 9018, NULL, 6525036354),(24, Birmingham, Bunnie, Ronald Regan, 84, NULL, 7946632892),(25, Rubens, Daisie, Pleasure, 2, NULL, 9348859564),(26, Halmkin, Clo, Holmberg, 907, NULL, 5532858557),(30, Bess, Stacee, Glendale, 73, NULL, 3683998533),(32, Petroselli, Ange, Norway Maple, 5, NULL, 6677897491),(33, Toghill, Charlotta, Randy, 867, NULL, 4666817217),(34, Twiggins, Catherina, Gulseth, 59, NULL, 7346109269),(35, Stogill, Hyatt, Summerview, 40376, NULL, 6589160233),(36, Lorryman, Tildy, Sachs, 34661, NULL, 3559599614),(37, Mouncher, Bernadine, Anthes, 4, NULL, 5729358607),(38, Plaster, Alfred, Warrior, 1, NULL, 9637168273),(40, Golda, Enos, Donald, 4533, NULL, 2579268728),(41, Stansby, Gail, Darwin, 6, NULL, 2089471105),(42, Wintringham, Mikol, Merchant, 8, NULL, 1447065997),(43, Patsall, Camilla, Randy, 7, NULL, 2331543454),(44, Munford, Kristal, Grover, 91, NULL, 7272878926),(45, Roskam, Jo-anne, Eastwood, 73492, NULL, 5893035934),(47, Jope, Allayne, Victoria, 19, NULL, 4637850275),(49, Schiefersten, Georgina, Westport, 57, NULL, 2509215441);")

# zweigstellen
cursor.execute("INSERT INTO `zweigstelle` (`zweigstellen_id`, `zweigstellenname`, `strasse`, `hausnummer`, `plz_id`, `telefonnr`, `steuernummer`) VALUES (NULL, 'Bremen', 'Kornstrasse', '50', '1', '468545', '457896435678');")
cursor.execute("INSERT INTO `zweigstelle` (`zweigstellen_id`, `zweigstellenname`, `strasse`, `hausnummer`, `plz_id`, `telefonnr`, `steuernummer`) VALUES (NULL, 'Bremen-Nord', 'Kreinsloger', '103', '2', '46821685', '946255862164');")

# kunden
cursor.execute("INSERT INTO kunden (kunden_id, nachname, vorname, strasse, hausnummer, plz_id, telefonnr) VALUES(3, Paolone, Esmeralda, Thompson, 9, NULL, 6796597538),(8, Arnott, Gav, Stuart, 28, NULL, 6227434475),(9, Cufley, Matt, Anzinger, 7105, NULL, 9299519814),(10, Mafham, Nan, Lerdahl, 35, NULL, 5851600596),(15, Broddle, Ange, Dawn, 68245, NULL, 2392422243),(16, Gerriet, Solly, Express, 650, NULL, 7137127474),(17, Adriaan, Chaddie, Haas, 5425, NULL, 9667451943),(19, Korf, Leo, Pawling, 15073, NULL,4649083462),(21, Firpo, Eldin, Vidon, 48, NULL, 5421111093),(22, Raybould, Farrel, Marcy, 6, NULL, 9435526452),(23, Barwack, Addison, Westerfield, 1, NULL, 1093115399),(24, Issitt, Lib, Dayton, 90, NULL, 9449537336),(25, Santos, Kakalina, Calypso, 773, NULL, 6264058613),(26, Caraher, Loralyn, North, 788, NULL, 9545610293),(28, Needham, Isidore, Fair Oaks, 172, NULL, 4687069297),(31, Maywood, Natalie, Randy, 1002, NULL, 2647718394),(32, Dibley, Winn, Buhler, 8, NULL, 8674186081),(33, Bucknall, Ida, High Crossing, 87777, NULL, 8921718014),(36, Vedenichev, Aurel, Lotheville, 9695, NULL, 6136367423),(39, Mighele, Wildon, Dakota, 7191, NULL, 1192429508),(40, De Filippis, Stevana, Ryan, 36955, NULL, 1106865818),(41, Briddle, Channa, Scofield, 6, NULL, 5535877461),(42, Stebbing, Ingaborg, Pine View, 58, NULL, 2482044636),(43, Gianelli, Rosanna, Farragut, 95219, NULL, 7183012385),(44, Sokale, Emmerich, Glacier Hill, 8949, NULL, 1411201853),(46, Jiruca, Cordelia, Carioca, 72923, NULL, 2917460214);")

# fahrzeug_preis
cursor.execute("USE fahrzeug_preis")
cursor.execute("INSERT INTO fahrzeug_preis (fahrzeug_preis_id, fahrzeug_preis_netto) VALUES(1, 249),(2, 249),(3, 249),(4, 249),(5, 249),(6, 249),(7, 249),(8, 249),(9, 249),(10, 249),(11, 249),(12, 249),(13, 249),(14, 249),(15, 249),(16, 249),(17, 249),(18, 249),(19, 249),(20, 249),(21, 249),(22, 249),(23, 249),(24, 249),(25, 249),(26, 249),(27, 249),(28, 249),(29, 249),(30, 249),(31, 249),(32, 249),(33, 249),(34, 249),(35, 249),(36, 249),(37, 249),(38, 249),(39, 249),(40, 249),(41, 249),(42, 249),(43, 249),(44, 249),(45, 249),(46, 249),(47, 249),(48, 249),(49, 249),(50, 249);")

# Fahrzeug
cursor.execute("INSERT INTO fahrzeug (fahrzeug_id, marke, klasse, status, kennzeichen, zweigstellen_id, fahrzeug_preis_id) VALUES(1, Hyundai, 1G4HR54K55U067447, 0, 337941276526984, NULL, NULL),(2, GMC, WDDDJ7CB2BA235314, 1, 6767570007245501, NULL, NULL),(3, Lexus, WAUDG94F15N652164, 0, 589376478750404713, NULL, NULL),(4, Chevrolet, JM3ER2A55C0139036, 1, 676299730455950849, NULL, NULL),(5, Hyundai, 3LNDL2L3XCR398991, 1, 5018556204712019028, NULL, NULL),(6, Chevrolet, JH4CU4F47AC106155, 1, 5602227314879099, NULL, NULL),(7, Chevrolet, SCBCP7ZA8AC301485, 1, 3558422937791107, NULL, NULL),(8, Subaru, 1G6AL5SX4D0571289, 0, 3531363267574477, NULL, NULL),(9, Mitsubishi, 1G4HD57208U022642, 0, 4751643427280714, NULL, NULL),(10, Chevrolet, JN1AZ4EH8FM961174, 0, 561045437851658445, NULL, NULL),(11, Saab, 1N6AD0CU2BC999873, 1, 5602214959990837, NULL, NULL),(12, Dodge, 2C3CCAKG2EH645440, 1, 3550588998214003, NULL, NULL),(13, Toyota, WVGAV3AX5EW186265, 1, 560224136608209826, NULL, NULL),(14, Mercedes-Benz, WVWGD7AJXEW340571, 1, 4405962730068925, NULL, NULL),(15, Nissan, WAUJT68E73A270160, 0, 3576408769968077, NULL, NULL),(16, Hummer, JN1CV6AP6AM131749, 1, 5048371497102309, NULL, NULL),(17, Subaru, 3N1BC1CP7CK320091, 0, 6331108737004604, NULL, NULL),(18, Isuzu, WBAUN1C5XBV124800, 0, 3565835694211574, NULL, NULL),(19, Chevrolet, 3VW4S7AT8EM819921, 0, 6767587899645374, NULL, NULL),(20, Pontiac, 2T1BU4EE0BC236536, 0, 3530756522072602, NULL, NULL),(21, Pontiac, 19UUA75627A432521, 0, 5100133035483178, NULL, NULL),(22, Mercedes-Benz, 1YVHZ8BA5A5862738, 1, 3577464645502936, NULL, NULL),(23, Kia, 5TFCW5F17DX681571, 0, 3585275339965258, NULL, NULL),(24, Subaru, JHMZE2H36ES320775, 0, 5528928590988162, NULL, NULL),(25, Chevrolet, 1N6AF0KY0EN247872, 0, 6762978877056954, NULL, NULL),(26, Chevrolet, WA1CV74L69D609007, 0, 6304561119138475404, NULL, NULL),(27, Mercury, 1G6DS5ED2B0880841, 0, 3562151344558114, NULL, NULL),(28, Scion, 1GYS4EEJ0BR695634, 1, 3547041892530260, NULL, NULL),(29, Honda, 19UUA56792A288180, 0, 5332431781852905, NULL, NULL),(30, BMW, WBS3C9C56FP731122, 1, 4405205506152782, NULL, NULL),(31, Isuzu, 3D7TT2CT9AG892600, 1, 560223920712612681, NULL, NULL),(32, Hummer, WAUWMAFC3FN064256, 1, 3557276590957129, NULL, NULL),(33, Cadillac, 1N6AD0CU6AC542420, 1, 5602256463171230, NULL, NULL),(34, Mercedes-Benz, 3GYT4LEFXCG180324, 0, 5100132981972184, NULL, NULL),(35, Chrysler, 2T1BURHE4EC870333, 0, 30412188389432, NULL, NULL),(36, Honda, 1G6AS5S32F0735934, 0, 6304544220205663930, NULL, NULL),(37, Infiniti, KM8JT3ACXAU115345, 1, 3553500988810200, NULL, NULL),(38, Mitsubishi, 1GD022CG6CZ690380, 0, 4917245511564705, NULL, NULL),(39, Ferrari, WAURMAFD9EN966091, 1, 4913645421983925, NULL, NULL),(40, Mercedes-Benz, 2D4RN3D10AR033717, 1, 4041590051681933, NULL, NULL),(41, Mazda, WAUAF48H19K898482, 1, 4041378600431, NULL, NULL),(42, Ferrari, 1G4HP54K034781652, 0, 4175004180761010, NULL, NULL),(43, Chevrolet, 3GYFNGEY0AS224747, 1, 3531412246920317, NULL, NULL),(44, Pontiac, WAUKFBFL5DA660052, 1, 3563215406081346, NULL, NULL),(45, Suzuki, JH4KB16697C496976, 1, 5579722850578195, NULL, NULL),(46, Hummer, YV4940BZ2E1735567, 1, 633110994181412601, NULL, NULL),(47, Volkswagen, WAUJF78K49N904867, 0, 3577699494508415, NULL, NULL),(48, Hyundai, WBALZ5C59CD749574, 0, 4041376027405, NULL, NULL),(49, Mitsubishi, 1G4GC5G36FF961304, 0, 3532483308894558, NULL, NULL),(50, Land Rover, WAUGL58E85A981390, 0, 3548846848040159, NULL, NULL);")
"""


# Menüs
def willkommen():
    choice = input("\n"
                   "    _______________WILLKOMMEN_______________\n"
                   "    |                 im                   |\n"
                   "    |   Python Projekt - Autovermietung    |\n"
                   "    |   2019 Copyright by. Frank Panzer    |\n"
                   "    |                                      |\n"
                   "    | Es werden alle Funktionen geladen... |\n"
                   "    | Es werden alle Datensätze geladen... |\n"
                   "    |                                      |\n"
                   "    |         Drücken Sie ENTER            |\n"
                   "    |  um alle Funktionen und Datensätze   |\n"
                   "    |  einzuspielen und ins Hauptmenü zu   |\n"
                   "    |  zu gelangen!                        |\n"
                   "    |______________________________________|\n"
                   "     ")
    print("\t Aktuelles Dateum und Uhrzeit")
    print(time.strftime("\t\t %d.%m.%Y %H:%M:%S"))
    time.sleep(2)


# H Menü
def hmenu() -> object:
    choice = input("\n"
                   "    ____________HAUPTMENUE______________\n"
                   "    |       A: Auflisten               |\n"
                   "    |       B: Anlegen                 |\n"
                   "    |       C: Entfernen               |\n"
                   "    |       D: Bearbeiten              |\n"
                   "    |       E: Kunden Optionen         |\n"
                   "    |----------------------------------|\n"
                   "    |       0: Beenden                 |\n"
                   "    |                                  |\n"
                   "    |__________________©_Frank_Panzer__|\n"
                   "\n"
                   "    Bitte treffe eine Wahl: ")

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
    choice = input("\n"
                   "        _________AUFLISTEN_MENÜ_____________\n"
                   "        |       A: Mitarbeiter auflisten   |\n"
                   "        |       B: Kunden auflisten        |\n"
                   "        |       C: Fahrzeuge auflisten     |\n"
                   "        |       D: Zweigstellen auflisten  |\n"
                   "        |----------------------------------|\n"
                   "        |       1: Hauptmenü               |\n"
                   "        |       0: Beenden                 |\n"
                   "        |                                  |\n"
                   "        |__________________©_Frank_Panzer__|\n"
                   "\n"
                   "        Bitte treffe eine Wahl: ")

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


# Alle Mitarbeiter anzeigen
def MitarbeiterAuflisten():
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


# Alle Kunden anzeigen
def KundenAuflisten():
    cursor.execute("SELECT * FROM kunden")
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

# Alle Fahrzeuge anzeigen
def FahrzeugeAuflisten():
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

# Alle Zweigstellen anzeigen
def ZweigstellenAuflisten():
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

# B Menü - Anlegen
def bmenue():
    choice = input('\n'
                   '        ___________ANLEGEN_MENÜ_____________\n'
                   '        |       A: Mitarbeiter anlegen     |\n'
                   '        |       B: Kunden anlegen          |\n'
                   '        |       C: Fahrzeuge anlegen       |\n'
                   '        |       D: Zweigstellen anlegen    |\n'
                   '        |----------------------------------|\n'
                   '        |       1: Hauptmenü               |\n'
                   '        |       0: Beenden                 |\n'
                   '        |                                  |\n'
                   '        |__________________©_Frank_Panzer__|\n'
                   '\n'
                   '        Bitte treffe eine Wahl: ')

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


# Abfragen um Mitarbeiter anzulegen
def MitarbeiterAnlegen():
    print("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
    input_mitarbeiter_nachname = input()
    liste_mitarbeiter = []
    liste_mitarbeiter.insert(1, input_mitarbeiter_nachname)

    print("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
    input_mitarbeiter_vorname = input()
    liste_mitarbeiter.insert(2, input_mitarbeiter_vorname)

    print("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
    input_mitarbeiter_strasse = input()
    liste_mitarbeiter.insert(3, input_mitarbeiter_strasse)

    print("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
    input_mitarbeiter_hausnummer = input()
    liste_mitarbeiter.insert(4, input_mitarbeiter_hausnummer)

    print("Bitte geben Sie eien Postleitzahl ein, die Sie hinzufügen wollen: ")
    liste_mitarbeiter_plz = []
    input_mitarbeiter_postleitzahl = input()
    liste_mitarbeiter_plz.insert(0, input_mitarbeiter_postleitzahl)
    liste_mitarbeiter_vergleich = []
    liste_mitarbeiter_vergleich.insert(0, input_mitarbeiter_postleitzahl)

    print("Bitte geben sie den Wohnort des neuen Mitarbeiters ein:")
    input_mitarbeiter_wohnort = input()
    liste_mitarbeiter_plz.insert(1, input_mitarbeiter_wohnort)

    print("Bitte geben sie die Telefonnummer des neuen Mitarbeiter ein:")
    input_mitarbeiter_telefonnummer = input()
    liste_mitarbeiter.insert(4, input_mitarbeiter_telefonnummer)

    liste_mitarbeiter.append(liste_mitarbeiter_vergleich[0])
    tupel_mitarbeiter: Tuple[str, ...] = tuple(liste_mitarbeiter)
    tupel_mitarbeiter_plz = tuple(liste_mitarbeiter_plz)

    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", tupel_mitarbeiter_plz)
    cursor.execute("INSERT INTO mitarbeiter (nachname, vorname, strasse, hausnummer, telefonnr, plz_id) VALUES (%s,"
                   "%s,%s,%s,%s, (SELECT plz_id FROM plz_id WHERE plz = %s limit 1))", tupel_mitarbeiter)
    DB_CBM.commit()
    print("Mitarbeiter erfolgreich angelegt.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


# Neuer Kunde anlegen
def KundenAnlegen():
    print("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
    input_kunde_nachname = input()
    liste_kunde = []
    liste_kunde.insert(1, input_kunde_nachname)

    print("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
    input_kunde_vorname = input()
    liste_kunde.insert(2, input_kunde_vorname)

    print("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
    input_kunde_strasse = input()
    liste_kunde.insert(3, input_kunde_strasse)

    print("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
    input_kunde_hausnummer = input()
    liste_kunde.insert(4, input_kunde_hausnummer)

    print("Bitte geben Sie eien Postleitzahl ein, die Sie hinzufügen wollen: ")
    liste_kunde_plz = []
    input_kunde_postleitzahl = input()
    liste_kunde_plz.insert(0, input_kunde_postleitzahl)
    liste_kunde_vergleich = []
    liste_kunde_vergleich.insert(0, input_kunde_postleitzahl)

    print("Bitte geben sie den Wohnort des neuen Mitarbeiters ein:")
    input_kunde_wohnort = input()
    liste_kunde_plz.insert(1, input_kunde_wohnort)

    print("Bitte geben sie die Telefonnummer des neuen Mitarbeiter ein:")
    input_kunde_telefonnummer = input()
    liste_kunde.insert(4, input_kunde_telefonnummer)

    liste_kunde.append(liste_kunde_vergleich[0])
    tupel_kunde = tuple(liste_kunde)
    tupel_kunde_plz = tuple(liste_kunde_plz)

    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", tupel_kunde_plz)
    cursor.execute(
        "INSERT INTO kunden (nachname, vorname, strasse, hausnummer, telefonnr, plz_id) VALUES (%s,%s,%s,%s,%s, (SELECT plz_id FROM plz_id WHERE plz = %s limit 1))",
        tupel_kunde)
    DB_CBM.commit()
    print("Kunde erfolgreich angelegt.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def view_zweigstelle_auswahl():
    cursor.execute("SELECT * FROM zweigstelle")
    result = cursor.fetchall()
    for row in result:
        print(f"zweigstellen_ID: {row[0]:5} zweigstellename: {row[1]:10}  ")

# Neue Fahrzeuge einfügen
def FahrzeugeAnlegen():
    global klasse
    print("Bitte geben sie die Marke des Fahrzeugs ein:")
    marke = input()
    liste_fahrzeuge = []
    liste_fahrzeuge.insert(0, marke)

    print(
        "Bitte wählen sie die Klasse des Fahrzeug aus\nLuxusklasse(1)\nMittelklasse(2)\nKleinwagen(3)\n")
    klasse_input = int(input())
    if klasse_input == 1:
        klasse = "Luxusklasse"
    if klasse_input == 2:
        klasse = "Mittelklasse"
    if klasse_input == 3:
        klasse = "Kleinwagen"
    liste_fahrzeuge.insert(1, klasse)

    print("Bitte geben sie das Kennzeichen des Fahrzeugs ein:")
    kennzeichen = input()
    liste_fahrzeuge.insert(2, kennzeichen)
    print("Bitte wählen sie die ID der Zweigstelle des Fahrzeuges: ")
    view_zweigstelle_auswahl()
    zweigstelle = input()
    liste_fahrzeuge_zweigstelle = []
    liste_fahrzeuge_zweigstelle.insert(0, zweigstelle)
    liste_fz_st_vergleich = []
    liste_fz_st_vergleich.insert(0, zweigstelle)

    print("Bitte wählen sie den Mietpreis aus")
    print("Folgende Mietpreise sind bereits angelegt:")

    cursor.execute("SELECT * FROM fahrzeug_preis")
    result = cursor.fetchall()
    for row in result:
        print(f"Preis ID: {row[0]:5} Nettopreis: {row[1]:5}")

    print("Bitte wählen Sie aus:\nNeuer Mietpreis festzulegen(0)\nVorhandener Mietpreis(1)\n")
    mietpreis_auswahl = int(input())

    if mietpreis_auswahl == 0:
        print("Bitte geben sie den neuen Mietpreis Preis ein: ")
    mietpreis = float(input())
    cursor.execute("INSERT INTO fahrzeug_preis (fahrzeug_preis_netto) VALUES (%s)", (mietpreis,))
    DB_CBM.commit()
    mietpreis_id_1 = cursor.execute("SELECT fahrzeug_preis_id FROM fahrzeug_preis WHERE fahrzeug_preis_netto = %s limit 2",(mietpreis,)).fetchall()
    mietpreis_id = mietpreis_id_1[0][0]

    if mietpreis_auswahl == 1:
        print("Folgende Mietpreise sind bereits angelegt: ")
    cursor.execute("SELECT * FROM fahrzeug_preis")
    result = cursor.fetchall()
    for row in result:
        print(f"Preis_ID: {row[0]:5} Nettopreis_pro_Tag: {row[1]:5}")
    print("Bitte wählen sie die gewünschte Preis_ID aus:")
    mietpreis_id = int(input())
    liste_fahrzeuge.append(liste_fz_st_vergleich[0])
    liste_fahrzeuge.append(mietpreis_id)
    tupel_fahrzeuge = tuple(liste_fahrzeuge)

    cursor.execute("INSERT INTO fahrzeug (marke, klasse, kennzeichen, zweigstellen_id, fahrzeug_preis_id) VALUES( % s, % s, % s, (SELECT zweigstellen_id FROM zweigstellee WHERE zweigstellen_id = % s limit 1), % s )", tupel_fahrzeuge)
    DB_CBM.commit()
    cursor.execute("INSERT INTO ausgeliehen_details (status, fahrzeug_id) VALUES (('frei'),(SELECT fahrzeug_id FROM fahrzeug WHERE kennzeichen = %s))", ((kennzeichen,)))
    DB_CBM.commit()
    print("Fahrzeug erfolgreich angelegt.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


def ZweigstellenAnlegen():
    print("Bitte geben Sie einen Zweigstellennamen an:")
    user_input_st_zweigstellenname = input()
    liste_zweigstelle = []
    liste_zweigstelle.insert(0, user_input_st_zweigstellenname)
    print("Bitte geben sie die Strasse der Zweigstelle ein:")
    user_input_st_strasse = input()
    liste_zweigstelle.insert(1, user_input_st_strasse)
    print("Bitte geben sie die Hausnummer der Zweigstelles ein:")
    user_input_st_hausnummer = input()
    liste_zweigstelle.insert(2, user_input_st_hausnummer)
    print("Bitte geben sie die Postleitzahl der Zweigstelles ein:")
    liste_zweigstelle_plz = []
    user_input_st_postleitzahl = input()
    liste_zweigstelle_plz.insert(0, user_input_st_postleitzahl)
    liste_st_vergleich = []
    liste_st_vergleich.insert(0, user_input_st_postleitzahl)
    print("Bitte geben sie den Ort der Zweigstelles ein:")
    user_input_st_ort = input()
    liste_zweigstelle_plz.insert(1, user_input_st_ort)
    print("Bitte geben sie die Telefonnummer der Zweigstelles ein:")
    user_input_st_telefonnummer = input()
    liste_zweigstelle.insert(3, user_input_st_telefonnummer)
    print("Bitte geben sie die Steuernummer der Zweigstelles ein:")
    user_input_st_steuernummer = input()
    liste_zweigstelle.insert(4, user_input_st_steuernummer)
    liste_zweigstelle.append(liste_st_vergleich[0])
    tupel_zweigstelle = tuple(liste_zweigstelle)
    tupel_zweigstelle_plz = tuple(liste_zweigstelle_plz)
    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", (tupel_zweigstelle_plz))
    cursor.execute("INSERT INTO zweigstelle (zweigstellenname,strasse, hausnummer, telefonnr, steuernummer, "
                   "plz_id) VALUES (%s,%s,%s,%s,%s, (SELECT plz_id FROM plz_id WHERE plz = %s limit 1))", tupel_zweigstelle)
    DB_CBM.commit()
    print("Zweigstelle erfolgreich angelegt.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


# C Menü - Entfernen
def cmenue():
    choice = input("\n"
                   "        ___________ENTFERNEN_MENUE__________\n"
                   "        |       A: Mitarbeiter entfernen   |\n"
                   "        |       B: Kunden entfernen        |\n"
                   "        |       C: Fahrzeuge entfernen     |\n"
                   "        |       D: Zweigstellen entfernen  |\n"
                   "        |----------------------------------|\n"
                   "        |       1: Hauptmenü               |\n"
                   "        |       0: Beenden                 |\n"
                   "        |                                  |\n"
                   "        |__________________©_Frank_Panzer__|\n"
                   "\n"
                   "        Bitte treffe eine Wahl: ")

    if choice == "A" or choice == "a":
        MitarbeiterEntfernen()
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


def MitarbeiterEntfernen():
    os.system("cls")
    cursor = DB_CBM.cursor()
    cursor.execute("SELECT * FROM mitarbeiter")
    result = cursor.fetchall()
    for row in result:
        print(f"Mitarbeiter ID: {row[0]}")
        print(f"Vorname: {row[2]}")
        print(f"Nachname: {row[1]}")
        print(f"Strasse: {row[3]}")
        print(f"Hausnummer: {row[4]}")
        print(f"Postleitzahl: {row[5]}")
        print(f"Telefonnummer: {row[6]}")
        print(f"\n")
    print("Liste der Kunden")
    MitarbeiterLoeschen = input("Bitte geben Sie die Kunden ID ein die Sie löschen möchten: ")
    cursor = DB_CBM.cursor()
    MitarbeiterLoeschenID = (MitarbeiterLoeschen,)
    cursor.execute("DELETE FROM mitarbeiter WHERE mitarbeiter_id = (%s)", (MitarbeiterLoeschen,))
    DB_CBM.commit()
    os.system("cls")
    print("Der Mitarbeiter wurde erfolgreich gelöscht.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def KundenEntfernen():
    os.system("cls")
    cursor = DB_CBM.cursor()
    cursor.execute("SELECT * FROM kunden")
    result = cursor.fetchall()
    for row in result:
        print(f"Kunden ID: {row[0]}")
        print(f"Vorname: {row[2]}")
        print(f"Nachname: {row[1]}")
        print(f"Strasse: {row[3]}")
        print(f"Hausnummer: {row[4]}")
        print(f"Telefonnummer: {row[6]}")
        print(f"\n")
    print("Liste der Kunden")
    FahrzeugLoeschen = input("Bitte geben Sie die Kunden ID ein die Sie löschen möchten: ")
    cursor = DB_CBM.cursor()
    FahrzeugLoeschenID = (FahrzeugLoeschen,)
    cursor.execute("DELETE FROM kunden WHERE kunden_id = (%s)", (FahrzeugLoeschen,))
    DB_CBM.commit()
    os.system("cls")
    print("Der Kunde wurde erfolgreich gelöscht.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


def FahrzeugeEntfernen():
    os.system("cls")
    cursor = DB_CBM.cursor()
    cursor.execute("SELECT * FROM fahrzeug")
    result = cursor.fetchall()
    for row in result:
        print(f"Fahrzeug ID: {row[0]}")
        print(f"Marke: {row[1]}")
        print(f"Klasse: {row[2]}")
        print(f"Status: {row[3]}")
        print(f"Kennzeichen: {row[4]}")
        print(f"\n")
    print("Liste der Fahrzeuge")
    FahrzeugLoeschen = input("Bitte geben Sie die Fahrzeug ID ein die Sie löschen möchten: ")
    cursor = DB_CBM.cursor()
    FahrzeugLoeschenID = (FahrzeugLoeschen,)
    cursor.execute("DELETE FROM fahrzeug WHERE fahrzeug_id = (%s)", (FahrzeugLoeschen,))
    DB_CBM.commit()
    os.system("cls")
    print("Das Fahrzeug wurde erfolgreich gelöscht.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


def ZweigstellenEntfernen():
    os.system("cls")
    cursor = DB_CBM.cursor()
    cursor.execute("SELECT * FROM zweigstelle")
    result = cursor.fetchall()
    for row in result:
        print(f"Zweigstellen ID: {row[0]}")
        print(f"Zweigstellen Name: {row[1]}")
        print(f"Strasse: {row[2]}")
        print(f"Hausnummer: {row[3]}")
        print(f"Telefonnr: {row[4]}")
        print(f"Steuernummer: {row[5]}")
        print(f"\n")
    print("Liste der Zweigstellen")
    ZweigstelleLoeschen = input("Bitte geben Sie die Zweigstellen ID ein die Sie löschen möchten: ")
    cursor = DB_CBM.cursor()
    ZweigstelleLoeschenID = (ZweigstelleLoeschen,)
    cursor.execute("DELETE FROM zweigstelle WHERE zweigstellen_id = (%s)", (ZweigstelleLoeschen,))
    DB_CBM.commit()
    os.system("cls")
    print("Die Zweigstelle wurde erfolgreich gelöscht.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


# D Menü Bearbeiten
def dmenue():
    choice = input("\n"
                   "        _________BEARBEITEN_MENUE___________\n"
                   "        |       A: Mitarbeiter bearbeiten  |\n"
                   "        |       B: Kunden bearbeiten       |\n"
                   "        |       C: Fahrzeuge bearbeiten    |\n"
                   "        |----------------------------------|\n"
                   "        |       1: Hauptmenü               |\n"
                   "        |       0: Beenden                 |\n"
                   "        |                                  |\n"
                   "        |__________________©_Frank_Panzer__|\n"
                   "\n"
                   "        Bitte treffe eine Wahl: ")

    if choice == "A" or choice == "a":
        MitarbeiterBearbeiten()
    elif choice == "B" or choice == "b":
        KundenBearbeiten()
    elif choice == "C" or choice == "c":
        FahrzeugeBearbeiten()
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
    print("Folgende Mitarbeiter sind vorhanden:")
    cursor.execute("SELECT * FROM mitarbeiter INNER JOIN plz_id ON mitarbeiter.plz_id=plz_id.plz_id INNER JOIN zweigstelle ON mitarbeiter.zweigstellen_id=zweigstelle.zweigstellen_id")
    result = cursor.fetchall()
    for row in result:
        print(
            f"MA_ID: {row[0]:4} Nachname: {row[1]:12} Vorname: {row[2]:12} Strasse: {row[3]:12} Hausnr.: {row[4]:4} PLZ: {row[9]:6} Ort: {row[10]:12} Telefon: {row[6]:15} Standort: {row[12]:10}")
    print("Bitte wählen sie die Mitarbeiter_ID (MA_ID) des Mitarbeiters dessen Daten sie ändern möchten")
    mitarbeiter_id = input()
    print("Bitte geben Sie den Nachnamen des Mitarbeiters ein:")
    user_input_m_nachname = input()
    print("Bitte geben sie den Vornamen des Mitarbeiters ein:")
    user_input_m_vorname = input()
    print("Bitte geben sie die Strasse des Mitarbeiters ein:")
    user_input_m_strasse = input()
    print("Bitte geben sie die Hausnummer des Mitarbeiters ein:")
    user_input_m_hausnummer = input()
    print("Bitte geben sie die Postleitzahl des Mitarbeiters ein:")
    liste_mitarbeiter_plz = []
    user_input_m_postleitzahl = input()
    liste_mitarbeiter_plz.insert(0, user_input_m_postleitzahl)
    print("Bitte geben sie den Wohnort des Mitarbeiters ein:")
    user_input_m_wohnort = input()
    liste_mitarbeiter_plz.insert(1, user_input_m_wohnort)
    print("Bitte geben sie die Telefonnummer des Mitarbeiter ein:")
    user_input_m_telefonnummer = input()
    print("Folgende zweigstelle sind verfügbar:")
    cursor.execute("SELECT zweigstellen_id, Zweigstellenname FROM zweigstelle")
    result = cursor.fetchall()
    for row in result:
        print(f" zweigstellen_id:{row[0]:5} Zweigstellenname: {row[1]:20}")
    print("Bitte wählen sie die zweigstellen_id des zweigstelle an dem der Mitarbeiter beschäftigt ist:")
    user_input_standortid = input()
    liste_mitarbeiter = []
    liste_mitarbeiter.append(user_input_m_nachname)
    liste_mitarbeiter.append(user_input_m_vorname)
    liste_mitarbeiter.append(user_input_m_strasse)
    liste_mitarbeiter.append(user_input_m_hausnummer)
    liste_mitarbeiter.append(user_input_m_telefonnummer)
    liste_mitarbeiter.append(user_input_standortid)
    liste_mitarbeiter.append(user_input_m_postleitzahl)
    liste_mitarbeiter.append(user_input_m_wohnort)
    liste_mitarbeiter.append(mitarbeiter_id)
    liste_mitarbeiter_standort = []
    liste_mitarbeiter_standort.append(user_input_standortid)
    liste_mitarbeiter_standort.append(mitarbeiter_id)
    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", (liste_mitarbeiter_plz))
    DB_CBM.commit()
    cursor.execute(
        """UPDATE mitarbeiter SET nachname=%s, vorname=%s, strasse=%s, hausnummer=%s, telefonnr=%s, zweigstellen_id=%s, plz_id=(SELECT plz_id FROM plz_id WHERE plz=%s AND ort=%s) WHERE mitarbeiter_id=%s",
        (liste_mitarbeiter))
    DB_CBM.commit()
    cursor.execute("UPDATE zweigstelle_mitarbeiter SET zweigstellen_id =%s WHERE mitarbeiter_id=%s",
                   (liste_mitarbeiter_standort))
    DB_CBM.commit()
    _id
    """)
    result = cursor.fetchall()
    for row in result:
        print(
            f"Mitarbeiter_ID: {row[0]:4} Nachname: {row[1]:12} Vorname: {row[2]:12} Strasse: {row[3]:12} Hausnr.: {row[4]:4} PLZ: {row[9]:6} Ort: {row[10]:12} Telefon: {row[6]:15} Standort: {row[12]:10}")
    print("Bitte wählen sie die Mitarbeiter_ID des Mitarbeiters dessen Daten sie ändern möchten")
    mitarbeiter_id = input()
    print("Bitte geben Sie den Nachnamen des Mitarbeiters ein:")
    user_input_m_nachname = input()
    print("Bitte geben sie den Vornamen des Mitarbeiters ein:")
    user_input_m_vorname = input()
    print("Bitte geben sie die Strasse des Mitarbeiters ein:")
    user_input_m_strasse = input()
    print("Bitte geben sie die Hausnummer des Mitarbeiters ein:")
    user_input_m_hausnummer = input()
    print("Bitte geben sie die Postleitzahl des Mitarbeiters ein:")
    liste_mitarbeiter_plz = []
    user_input_m_postleitzahl = input()
    liste_mitarbeiter_plz.insert(0, user_input_m_postleitzahl)
    print("Bitte geben sie den Wohnort des Mitarbeiters ein:")
    user_input_m_wohnort = input()
    liste_mitarbeiter_plz.insert(1, user_input_m_wohnort)
    print("Bitte geben sie die Telefonnummer des Mitarbeiter ein:")
    user_input_m_telefonnummer = input()
    print("Folgende zweigstelle sind verfügbar:")
    cursor.execute("SELECT zweigstellen_id, Zweigstellenname FROM zweigstelle")
    result = cursor.fetchall()
    for row in result:
        print(f" zweigstellen_id:{row[0]:5} Zweigstellenname: {row[1]:20}")
    print("Bitte wählen sie die zweigstellen_id des zweigstelle an dem der Mitarbeiter beschäftigt ist:")
    user_input_standortid = input()
    liste_mitarbeiter = []
    liste_mitarbeiter.append(user_input_m_nachname)
    liste_mitarbeiter.append(user_input_m_vorname)
    liste_mitarbeiter.append(user_input_m_strasse)
    liste_mitarbeiter.append(user_input_m_hausnummer)
    liste_mitarbeiter.append(user_input_m_telefonnummer)
    liste_mitarbeiter.append(user_input_standortid)
    liste_mitarbeiter.append(user_input_m_postleitzahl)
    liste_mitarbeiter.append(user_input_m_wohnort)
    liste_mitarbeiter.append(mitarbeiter_id)
    liste_mitarbeiter_standort = []
    liste_mitarbeiter_standort.append(user_input_standortid)
    liste_mitarbeiter_standort.append(mitarbeiter_id)
    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", (liste_mitarbeiter_plz))
    DB_CBM.commit()
    cursor.execute(
        "UPDATE mitarbeiter SET nachname=%s, vorname=%s, strasse=%s, hausnummer=%s, telefonnr=%s, zweigstellen_id=%s, plz_id=(SELECT plz_id FROM plz_id WHERE plz=%s AND ort=%s) WHERE mitarbeiter_id=%s",
        (liste_mitarbeiter))
    DB_CBM.commit()
    cursor.execute("UPDATE zweigstelle_mitarbeiter SET zweigstellen_id =%s WHERE mitarbeiter_id=%s",
                   (liste_mitarbeiter_standort))
    DB_CBM.commit()
    print("Der Mitarbeiter wurde erfolgreich bearbeitet.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


def KundenBearbeiten():
    print("Folgende Kunden sind vorhanden:")
    cursor.execute("SELECT * FROM kunden INNER JOIN plz_id ON kunden.plz_id=plz_id.plz_id")
    result = cursor.fetchall()
    for row in result:
        print(
            f"Kunden_ID: {row[0]:5} Nachname: {row[1]:15} Vorname: {row[2]:15} Strasse: {row[3]:15} Hausnr.: {row[4]:5} PLZ: {row[8]:8} Ort: {row[9]:15} Telefon: {row[6]:15}")
    print("Bitte wählen sie die Kunden_ID des zu ändernden Kunden:")
    kunde_id = input()
    liste_kunde_1 = []
    print("Bitte geben sie den Nachnamen des Kunden ein:")
    user_input_k_nachname = input()
    liste_kunde_1.insert(0, user_input_k_nachname)
    print("Bitte geben sie den Vornamen des Kunden ein:")
    user_input_k_vorname = input()
    liste_kunde_1.insert(1, user_input_k_vorname)
    print("Bitte geben sie die Strasse des Kunden ein:")
    user_input_k_strasse = input()
    liste_kunde_1.insert(2, user_input_k_strasse)
    print("Bitte geben sie die Hausnummer des Kunden ein:")
    user_input_k_hausnummer = input()
    liste_kunde_1.insert(3, user_input_k_hausnummer)
    print("Bitte geben sie die Postleitzahl des Kunden ein:")
    liste_kunde_plz = []
    user_input_k_postleitzahl = input()
    liste_kunde_1.insert(5, user_input_k_postleitzahl)
    liste_kunde_plz.insert(0, user_input_k_postleitzahl)
    print("Bitte geben sie den Wohnort des Kunden ein:")
    user_input_k_wohnort = input()
    liste_kunde_1.insert(6, user_input_k_wohnort)
    liste_kunde_plz.insert(1, user_input_k_wohnort)
    print("Bitte geben sie die Telefonnummer des Kunden ein:")
    user_input_k_telefonnummer = input()
    liste_kunde_1.insert(4, user_input_k_telefonnummer)
    liste_kunde_1.insert(7, kunde_id)
    cursor.execute("INSERT INTO plz_id (plz, ort) VALUES (%s,%s)", (liste_kunde_plz))
    cursor.execute(
        "UPDATE kunden SET nachname=%s, vorname=%s, strasse=%s, hausnummer=%s, telefonnr=%s, plz_id=(SELECT plz_id FROM plz_id WHERE plz=%s AND ort=%s) WHERE kunden_id=%s",
        (liste_kunde_1))
    DB_CBM.commit()
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def FahrzeugeBearbeiten():
    print("Folgende Fahrzeuge sind vorhanden:")
    cursor.execute(
        "SELECT * FROM fahrzeug INNER JOIN zweigstelle ON fahrzeug.zweigstelle_ID = zweigstelle.zweigstelle_ID INNER JOIN fahrzeug_preis ON Fahrzeug.fahrzeug_preis_id = fahrzeug_preis.Fahrzeug_preis_id")
    result = cursor.fetchall()
    for row in result:
        print(
            f"Fahrzeug_ID: {str(row[0]):5} Marke: {str(row[1]):18} Klasse: {str(row[2]):15} Kennzeichen: {str(row[3]):15} Standort: {str(row[7]):} Tagespreis netto: {str(row[14]):20} ")
    print("Bitte wählen sie die Fahrzeug_ID des zu ändernden Fahrzeugs:")
    liste_fahrzeuge = []
    Fahrzeug_id = input()
    liste_fahrzeuge.insert(5, Fahrzeug_id)
    print("Bitte geben sie die Marke des Fahrzeugs ein:")
    marke = input()
    liste_fahrzeuge.insert(0, marke)
    print(
        "Bitte wählen sie die Klasse des Fahrzeugs aus (1) für Luxusklasse, (2) für Mittelklasse, (3) für Kleinwagen:")
    klasse_input = int(input())
    if klasse_input == 1:
        klasse = "Luxusklasse"
    if klasse_input == 2:
        klasse = "Mittelklasse"
    if klasse_input == 3:
        klasse = "Kleinwagen"
    liste_fahrzeuge.insert(1, klasse)
    print("Bitte geben sie das Kennzeichen des Fahrzeugs ein:")
    kennzeichen = input()
    liste_fahrzeuge.insert(2, kennzeichen)
    print("Bitte wählen sie den Standort des Fahrzeugs (zur Auswahl nutzen sie bitte die Zweigstelle_ID):")
    view_zweigstelle_auswahl()
    standort = input()
    liste_fahrzeuge.insert(3, standort)
    print("Bitte wählen sie den Mietpreis aus")
    print("Folgende Mietpreise sind bereits angelegt: ")
    cursor.execute("SELECT * FROM Fahrzeug_preis")
    result = cursor.fetchall()
    for row in result:
        print(f"Preis_ID: {row[0]:5} Nettopreis: {row[1]:5}")
    print("Um einen neuen Mietpreis festzulegen, geben sie bitte die (0) ein, um einen bereits festgelegten Preis zu nutzen geben sie bitte die(1) ein: ")
    mietpreis_auswahl = int(input())
    if mietpreis_auswahl == 0:
        print("Bitte geben sie den gewünschten Preis an:")
    mietpreis = float(input())
    cursor.execute("INSERT INTO Fahrzeug_preis (Fahrzeug_preis_netto) VALUES (%s)", (mietpreis,))
    DB_CBM.commit()
    cursor.execute("SELECT Fahrzeug_preis_id FROM Fahrzeug_preis WHERE Fahrzeug_preis_netto = %s limit 1", (mietpreis,))
    result = cursor.fetchone()
    mietpreis_id = result[0]
    if mietpreis_auswahl == 1:
        print("Folgende Mietpreise sind bereits angelegt:")
    cursor.execute("SELECT * FROM Fahrzeug_preis")
    result = cursor.fetchall()
    for row in result:
        print(f"Preis_ID: {row[0]:5} Nettopreis_pro_Tag: {row[1]:5}")
    print("Bitte wählen sie die gewünschte Preis_ID aus:")
    mietpreis_id = int(input())
    liste_fahrzeuge.insert(4, mietpreis_id)
    cursor.execute(
        "UPDATE Fahrzeug SET marke=%s, klasse=%s, kennzeichen=%s, Zweigstelle_ID=%s, Fahrzeug_preis_id=%s WHERE Fahrzeug_id=%s",
        liste_fahrzeuge)
    DB_CBM.commit()
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


# E Menü - Kunden Optionen
def emenue():
    choice = input("\n"
                   "        _________KUNDEN_OPTIONEN___________________\n"
                   "        |       A: Fahrzeug Ausleihen              |\n"
                   "        |       B: Fahrzeug Zurückgeben            |\n"
                   "        |       C: Fahrzeug sotieren nach Status   |\n"
                   "        |       D: Fahrzeug sotieren nach Modell   |\n"
                   "        |       E: Schadensbericht einreichen      |\n"
                   "        |------------------------------------------|\n"
                   "        |       1: Hauptmenü                       |\n"
                   "        |       0: Beenden                         |\n"
                   "        |                                          |\n"
                   "        |__________________________©_Frank_Panzer__|\n"
                   "\n"
                   "        Bitte treffe eine Wahl: ")

    if choice == "A" or choice == "a":
        FahrzeugAusleihen()
    elif choice == "B" or choice == "b":
        FahrzeugZurueckgeben()
    elif choice == "C" or choice == "c":
        FahrzeugSotierenStatus()
    elif choice == "D" or choice == "d":
        FahrzeugSotierenModell()
    elif choice == "E" or choice == "e":
        FahrzeugSchadensbericht()
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
    print("Das Fahrzeug ausleihen habe ich mit etlichen Varianten gecodet, jedoch kamen bei allen nur Fehler raus.\nSo das ich den Code wieder entfernte.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def FahrzeugZurueckgeben():
    print("Sie möchten ein Fahrzeug zurück bringen. Folgende Fahrzeuge sind vorhanden:")
    cursor.execute("SELECT * FROM fahrzeug")
    result = cursor.fetchall()
    for row in result:
        print(
            f"fahrzeug_ID: {str(row[0]):5} Marke: {str(row[1]):10} Klasse: {str(row[2]):15} Kennzeichen: {str(row[3]):15} ")
    print("Bitte wählen sie die fahrzeug_ID des Fahrzeugs, das sie zurück bringen möchten:")
    fahrzeug_id = input()
    stand_fahrzeug = []
    stand_fahrzeug.insert(1, fahrzeug_id)
    print("Folgende zweigstelle stehen zur Rückgabe zur Verfügung:")
    cursor.execute("SELECT * FROM zweigstelle")
    result = cursor.fetchall()
    for row in result:
        print(f"zweigstelle_ID: {row[0]:5} zweigstellename: {row[1]:25}")
    print("Bitte wählen sie die zweigstelle_ID des annehmenden zweigstelles aus:")
    stand_id = input()
    stand_fahrzeug.insert(0, stand_id)
    cursor.execute("UPDATE fahrzeug SET zweigstellen_id = %s WHERE fahrzeug_id = %s", stand_fahrzeug)
    DB_CBM.commit()
    print("Das Fahrzeug wurde erfolgreich abgegeben.")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def FahrzeugSotierenStatus():
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


def FahrzeugSotierenModell():
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
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()

def FahrzeugSchadensbericht():
    Schadensbericht = open('Schadensbericht.txt', 'a')
    Schadensbericht_input = input("Schaden: ")
    print(Schadensbericht_input, file=Schadensbericht)
    Schadensbericht.close()
    os.system("cls")
    print("")
    print("Herzlichen Dank für Ihren Schadensbericht!")
    print("")
    choice = input("Bitte wählen Sie:\n- Hauptmenü (1)\n- Programm Beenden(0)\n")
    if choice == "1":
        hmenu()
    elif choice == "0":
        sys.exit()


willkommen()
hmenu()
