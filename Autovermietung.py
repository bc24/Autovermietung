'''
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Installieren
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

Quellen
Menü              -   http://effbot.org/tkinterbook/menu.htm
MySQL Connector   -   https://pypi.org/project/mysql-connector-python/

'''
# Importe
import mysql
import mysql.connector
from tkinter import *

# Datenbank MySQL
DB_CBM=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cbm_Autovermietung"
)
mycursor = DB_CBM.cursor()

# SQL Tabelle mitarbeiter erstellen
mycursor.execute("CREATE TABLE mitarbeiter(mitarbeiter_id INTEGER PRIMARY KEY AUTOINCREMENT,vorname VARCHAR(30),nachname VARCHAR(50),strasse VARCHAR(80),hausnummer INTEGER,plz_id INTEGER,telefonnr VARCHAR(80),FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") #IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle zweigstellen erstellen
mycursor.execute("CREATE TABLE zweigstellen (standort_id INTEGER PRIMARY KEY AUTOINCREMENT,strasse VARCHAR(80),plz_id INTEGER,hausnummer INTEGER,telefonnr INTEGER,steuernummer VARCHAR(20), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle zweigstellen_mitarbeiter erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS zweigstellen_mitarbeiter(standort_id INTEGER, mitarbeiter_id INTEGER, FOREIGN KEY (standort_id) REFERENCES standorte(standort_id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (mitarbeiter_id) REFERENCES mitarbeiter(mitarbeiter_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle kunde erstellen
mycursor.execute("CREATE TABLE IF NOT EXISTS kunden(kunden_id INTEGER PRIMARY KEY AUTOINCREMENT, vorname VARCHAR(30), nachname VARCHAR(50), strasse VARCHAR(80), hausnummer INTEGER, plz_id INTEGER, telefonnr VARCHAR(80), FOREIGN KEY (plz_id) REFERENCES plz_id(plz_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle fahrzeuge erstellen
mycursor.execute("CREATE TABLE fahrzeuge(kfz_id INTEGER PRIMARY KEY AUTOINCREMENT,marke VARCHAR(50),modell VARCHAR(50),status VARCHAR(30),kennzeichen VARCHAR(11),standort_id INTEGER, kfz_preis_id INTEGER,FOREIGN KEY (standort_id) REFERENCES standorte(standort_id) ON UPDATE CASCADE ON DELETE SET NULL,FOREIGN KEY (kfz_preis_id) REFERENCES kfr_preis(kfz_preis_id) ON UPDATE CASCADE ON DELETE SET NULL)") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle plz_id erstellen
mycursor.execute("CREATE TABLE plz_id (plz_id INTEGER PRIMARY KEY AUTOINCREMENT,plz CHAR(5), ort varchar(50))") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# SQL Tabelle plz_id erstellen
mycursor.execute("CREATE TABLE plz_id (plz_id INTEGER PRIMARY KEY AUTOINCREMENT,plz CHAR(5), ort varchar(50))") # IF NOT EXISTS
DB_CBM.close()
DB_CBM.commit()

# Menü 1
# Übersicht über die vorhandenen Fahrzeuge

def menuepunkt1():
  mycursor = DB_CBM.cursor()
  mycursor.execute("SELECT * FROM `autovermietung` WHERE `fahrzeuge`")
  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)

# Menü 2
# Neue Fahrzeuge einfügen

def menuepunkt2():
  Fahrzeuge_Anlegen=input("Bitte geben Sie eine Automarkte ein die Sie hinzufügen wollen: ")
  mycursor = DB_CBM.cursor()
  mycursor.execute("INSERT INTO fahrzeuge (fahrzeugmarken) VALUES (%s)", (Fahrzeuge_Anlegen,) )
  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)


## Menü Fahrzeuge                               #Hauptmenü 0
#   |  
#   |- Fahrzeuge auflisten                      #1
#   |- Neue Fahrzeuge                           #2
#   |- Fahrzeuge entfernen                      #3
#   |- Fahrzeuge bearbeiten                     #4
#   |- Mietpreise für Fahrzeuge festlegen       #5
#   |- Sortierung der Fahrzeuge                 #6
#       |- Modell                               #7
#       |- Status                               #8
#       |- Vorhanden                            #9              ###### Weiter Bearbeiten
#       |- Verliehen                            #10
#   |- Mitarbeiter                              #11
#       |- Alle Mitarbeiter anzeigen            #12
#       |- Mitarbeiter anlegen                  #13
#       |- Mitarbeiter ändern                   #14
#   |- Kunde                                    #15
#       |- Alle Kunden anzeigen                 #16
#       |- Neuer Kunde anlegen                  #17
#       |- Kunde ändern                         #18
#   |- Kundenoptionen                           #19
#       |- Fahrzeug leihen                      #20
#       |- Fahrzeug zurückbringen               #21
#       |- Fahrzeug zustand                     #22
#           |- Fahrzeug beschädigt              #23
#           |- Fahrzeug zerstört                #24


# Notiz an mich
'''
FahrzeugSortierung
FahrzeugSortierungModell
FahrzeugSortierungStatus

VorhandenVerliehen
Mitarbeiter
AlleMitarbeiterAnzeigen
MitarbeiterAnlegen
MitarbeiterAendern

Kunde
AlleKundenAnzeigen
NeuerKundeAnlegen
KundeAendern

KundenoptionenMenu
FahrzeugLeihen
FahrzeugZurueckbringen
FahrzeugZustand
FahrzeugBeschaedigt 
FahrzeugZerstoert

'''




# Menü
root = Tk()
menubar = Menu(root)

# Fahrzeug Menü - Umsetzung

def FahrzeugeAuflisten():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt1())
  button.pack()

def NeueFahrzeuge():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt2())
  button.pack()

  #

def FahrzeugeEntfernen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt3())
  button.pack()

def FahrzeugeBearbeiten():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt4())
  button.pack()

def FahrzeugMietpreise():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt5())
  button.pack()

def FahrzeugSortierung():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt6())
  button.pack()

def FahrzeugSortierungModell():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt7())
  button.pack()

def FahrzeugSortierungStatus():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt8())
  button.pack()


# Mitarbeiter Menü - Umsetzung
def VorhandenVerliehen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt9())
  button.pack()

def Mitarbeiter():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt10())
  button.pack()

def AlleMitarbeiterAnzeigen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt11())
  button.pack()

def MitarbeiterAnlegen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt12())
  button.pack()

def MitarbeiterAendern():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt13())
  button.pack()

# Kunde Menü - Umsetzung

def Kunde():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt14())
  button.pack()


Label(root,
		 text="Projekt Autovermietung in Python",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()      # .pack  =  Minimal und Maximal Größe des Textfeldes

Label(root,
		 text="Von Frank Panzer",
		 fg = "red",
		 font = "Times").pack()

Label(root,
		 text="2019",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

# Fahrzeug Menü
fahrzeuge = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fahrzeuge", menu=fahrzeuge)
fahrzeuge.add_command(label="Fahrzeuge auflisten", command=FahrzeugeAuflisten)
fahrzeuge.add_command(label="Neue Fahrzeuge", command=NeueFahrzeuge)
fahrzeuge.add_command(label="Fahrzeuge entfernen", command=FahrzeugeEntfernen)
fahrzeuge.add_command(label="Fahrzeuge bearbeiten", command=FahrzeugeBearbeiten)
fahrzeuge.add_command(label="Mietpreise für Fahrzeuge festlegen", command=FahrzeugMietpreise)
fahrzeuge.add_command(label="Sortierung der Fahrzeuge", command=FahrzeugSortierung)
fahrzeuge.add_separator()  # Einen Strich ziehen
fahrzeuge.add_cascade(label="Beenden", command=root.quit)

# Mitarbeiter Menü
mitarbeiter = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Mitarbeiter", menu=mitarbeiter)
mitarbeiter.add_command(label="Alle Mitarbeiter anzeigen", command=AlleMitarbeiter)
mitarbeiter.add_command(label="Mitarbeiter anlegen", command=MitarbeiterAnlegen)
mitarbeiter.add_command(label="Mitarbeiter ändern", command=MitarbeiterAendern)
mitarbeiter.add_separator()  # Einen Strich ziehen
mitarbeiter.add_cascade(label="Beenden", command=root.quit)

# Kunden Menü
kunde = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kunde", menu=kunde)
kunde.add_command(label="Alle Mitarbeiter anzeigen", command=donothing)
kunde.add_command(label="Neuer Kunde anlegen", command=donothing)
kunde.add_command(label="Kunde ändern", command=donothing)
kunde.add_separator()  # Einen Strich ziehen
kunde.add_cascade(label="Beenden", command=root.quit)

# Kundenoptionen Menü
kundenoptionen = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kundenoptionen", menu=kundenoptionen)
kundenoptionen.add_command(label="Fahrzeug leihen", command=donothing)
kundenoptionen.add_command(label="Fahrzeug zurückbringen", command=donothing)
kundenoptionen.add_command(label="Fahrzeug zustand", command=donothing)
kundenoptionen.add_command(label="Fahrzeug beschädigt", command=donothing)
kundenoptionen.add_command(label="Fahrzeug zerstört", command=donothing)
kundenoptionen.add_separator()  # Einen Strich ziehen
kundenoptionen.add_cascade(label="Beenden", command=root.quit)

menubar.add_cascade(label=" 2019 by. Frank Panzer")

root.config(menu=menubar)
root.mainloop()
