#
# Installieren
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

# Quellen
# Menü -  https://www.python-kurs.eu/tkinter_labels.php
#         https://www.tutorialspoint.com/python3/tk_menu.htm
#

# Importe
import mysql.connector
from tkinter import *

# Datenbank MySQL
DB_CBM = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cbm_Autovermietung"
)

## Abfragen
# Übersicht über die vorhandenen Fahrzeuge
# Durch das eingeben vom Wort Fahrzeuge werden alle Fahrzeuge aufgelistet

# Menü 1
# Übersicht über die vorhandenen Fahrzeuge

mycursor = DB_CBM.cursor()
mycursor.execute("SELECT * FROM `autovermietung` WHERE `Fahrzeuge`")
myresult = mycursor.fetchall()

for x in myresult:
  print("Das sind alle Fahrzeuge: ", x)

# Menü 2
# Neue Fahrzeuge einfügen




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
#           |- Vorhanden/Verliehen              #9
#   |- Mitarbeiter                              #10
#       |- Alle Mitarbeiter anzeigen            #11
#       |- Mitarbeiter anlegen                  #12
#       |- Mitarbeiter ändern                   #13
#   |- Kunde                                    #14
#       |- Alle Kunden anzeigen                 #15
#       |- Neuer Kunde anlegen                  #16
#       |- Kunde ändern                         #17
#   |- Kundenoptionen                           #18
#       |- Fahrzeug leihen                      #19
#       |- Fahrzeug zurückbringen               #19
#       |- Fahrzeug zustand                     #20
#           |- Fahrzeug beschädigt              #21
#           |- Fahrzeug zerstört                #22


#Menü # Quelle: https://www.python-kurs.eu/tkinter_labels.php
def donothing():
  filewin = Toplevel(root)
  button = Button(filewin, text="Do nothing button")
  button.pack()


root = Tk()
menubar = Menu(root)


Label(root,
		 text="Projekt Autovermietung in Python",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
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
fahrzeuge.add_command(label="Fahrzeuge auflisten", command=donothing)
fahrzeuge.add_command(label="Neue Fahrzeuge", command=donothing)
fahrzeuge.add_command(label="Fahrzeuge entfernen", command=donothing)
fahrzeuge.add_command(label="Fahrzeuge bearbeiten", command=donothing)
fahrzeuge.add_command(label="Mietpreise für Fahrzeuge festlegen", command=donothing)
fahrzeuge.add_command(label="Sortierung der Fahrzeuge", command=donothing)
fahrzeuge.add_separator()  # Einen Strich ziehen
fahrzeuge.add_cascade(label="Beenden", command=root.quit)

# Mitarbeiter Menü
mitarbeiter = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Mitarbeiter", menu=mitarbeiter)
mitarbeiter.add_command(label="Alle Mitarbeiter anzeigen", command=donothing)
mitarbeiter.add_command(label="Mitarbeiter anlegen", command=donothing)
mitarbeiter.add_command(label="Mitarbeiter ändern", command=donothing)
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
