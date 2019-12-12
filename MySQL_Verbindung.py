'''
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

Quellen
Menü                -   http://effbot.org/tkinterbook/menu.htm
MySQL Connector     -   https://pypi.org/project/mysql-connector-python/
Foreign Keys        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze  -   https://mockaroo.com/


'''
# Datenbank MySQL Verbindung
DB_CBM = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "cbm_Autovermietung"
)

# mycursor Cursor holen
mycursor = DB_CBM.cursor()

# cbm_Autovermietung Datenbank anlegen
mycursor.execute("CREATE DATABASE IF NOT EXISTS cbm_Autovermietung")

# Überprüfen ob Datenbank schon existiert
mycursor.execute("SHOW DATABASES LIKE 'cbm_A%'")
for x in mycursor:
  print("Vorhandene Datenbank",x)

# Datenbank Tabelle plz_ip erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS plz_id ( plz_id INT PRIMARY KEY AUTO_INCREMENT, plz VARCHAR(5) DEFAULT NULL, ort VARCHAR(50) DEFAULT NULL )")

# Datenbank Tabelle mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS mitarbeiter(mitarbeiter_id INTEGER PRIMARY KEY AUTO_INCREMENT,vorname VARCHAR(50),nachname VARCHAR(50),strasse VARCHAR(80),hausnummer INTEGER,plz_id INTEGER,telefonnr VARCHAR(50),FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstelle (zweigstellen_id INTEGER PRIMARY KEY AUTO_INCREMENT, strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr INTEGER, steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle zweigstellen_mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstellen_mitarbeiter (zweigstellen_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle kunden erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS kunden (kunden_id INTEGER PRIMARY KEY AUTO_INCREMENT, nachname VARCHAR(50), vorname VARCHAR(30), strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(80), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug_preis (fahrzeug_preis_id INTEGER PRIMARY KEY AUTO_INCREMENT, fahrzeug_id INTEGER, fahrzeug_preis_netto FLOAT)")

# Datenbank Tabelle fahrzeug erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug (fahrzeug_id INTEGER PRIMARY KEY AUTO_INCREMENT, marke VARCHAR(50), modell VARCHAR(50), status VARCHAR(30), kennzeichen VARCHAR(20), zweigstellen_id INTEGER, fahrzeug_preis_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_preis_id) REFERENCES fahrzeug_preis(fahrzeug_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle fahrzeug_preis Fremdschlüssel erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS fahrzeug_preis (FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS rechnung (rechnung_id INTEGER PRIMARY KEY AUTO_INCREMENT, zweigstellen_id INTEGER, kunden_id INTEGER, FOREIGN KEY (zweigstellen_id) REFERENCES zweigstelle(zweigstellen_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (kunden_id) REFERENCES kunden(kunden_id) ON UPDATE CASCADE ON DELETE SET NULL)")

# Datenbank Tabelle rechnung_details erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS rechnung_details (rechnung_id INTEGER, fahrzeug_id INTEGER, verleih_beginn DATE, verleih_ende DATE, FOREIGN KEY (rechnung_id) REFERENCES rechnung(rechnung_id) ON UPDATE CASCADE ON DELETE SET NULL, FOREIGN KEY (fahrzeug_id) REFERENCES fahrzeug(fahrzeug_id) ON UPDATE CASCADE ON DELETE SET NULL)")
