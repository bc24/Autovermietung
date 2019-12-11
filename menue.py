
# Menü start

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



# Menü
root = Tk()
menubar = Menu(root)

# Menü def Start

# Fahrzeug Menü - Umsetzung
def FahrzeugeAuflisten():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt1())
  button.pack()

def NeueFahrzeuge():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt2())
  button.pack()

# Ab hier weiter mit dem Menü
#############################################
def FahrzeugeEntfernen():
  filewin = Topleve1(root)
  button = Button(filewin, text= menuepunkt3())

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

# Fahrzeug vorhanden Menü - Umsetzung
def Vorhanden():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt9())
  button.pack()

# Fahrzeug verliehen Menü - Umsetzung
def Verliehen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt10())
  button.pack()

def Mitarbeiter():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt11())
  button.pack()

def AlleMitarbeiterAnzeigen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt12())
  button.pack()

def MitarbeiterAnlegen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt13())
  button.pack()

def MitarbeiterAendern():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt14())
  button.pack()

# Kunde Menü - Umsetzung

def Kunde():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt15())
  button.pack()

# Alle Kunden anzeigen Menü - Umsetzung

def AlleKundenAnzeigen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt16())
  button.pack()

# Neuer Kunde anlegen Menü - Umsetzung

def NeuerKundeAnlegen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt17())
  button.pack()

# Kunde ändern Menü - Umsetzung

def KundeAendern():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt18())
  button.pack()

# Kundenoptionen Menu - Umsetzung

def KundenoptionenMenu():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt19())
  button.pack()

# Fahrzeug Leihmenü - Umsetzung

def FahrzeugLeihen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt20())
  button.pack()

# Fahrzeug zurück bringen Menü - Umsetzung

def FahrzeugZurueckbringen():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt21())
  button.pack()

# Fahrzeug Zustand Menü - Umsetzung

def FahrzeugZustand():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt22())
  button.pack()

# Fahrzeug Beschädigt  Menü - Umsetzung

def FahrzeugBeschaedigt ():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt23())
  button.pack()

# Fahrzeug zerstört Menü - Umsetzung

def FahrzeugZerstoert():
  filewin = Toplevel(root)
  button = Button(filewin, text="Dieser Menüpunkt ist noch nicht fertig!"+ menuepunkt24())
  button.pack()

# Menü def Ende


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
mitarbeiter.add_command(label="Mitarbeiter anlegen", command=MitarbeiterAnlegen)
mitarbeiter.add_command(label="Mitarbeiter ändern", command=MitarbeiterAendern)
mitarbeiter.add_separator()  # Einen Strich ziehen
mitarbeiter.add_cascade(label="Beenden", command=root.quit)

# Kunden Menü
kunde = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kunde", menu=kunde)
kunde.add_command(label="Alle Kunden anzeigen", command=AlleKundenAnzeigen)
kunde.add_command(label="Neuer Kunde anlegen", command=NeuerKundeAnlegen)
kunde.add_command(label="Kunde ändern", command=KundeAendern)
kunde.add_separator()  # Einen Strich ziehen
kunde.add_cascade(label="Beenden", command=root.quit)

# Kundenoptionen Menü
kundenoptionen = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kundenoptionen", menu=kundenoptionen)
kundenoptionen.add_command(label="Fahrzeug leihen", command=FahrzeugLeihen)
kundenoptionen.add_command(label="Fahrzeug zurückbringen", command=FahrzeugZurueckbringen)
kundenoptionen.add_command(label="Fahrzeug zustand", command=FahrzeugZustand)
kundenoptionen.add_command(label="Fahrzeug beschädigt", command=FahrzeugBeschaedigt)
kundenoptionen.add_command(label="Fahrzeug zerstört", command=FahrzeugZerstoert)
kundenoptionen.add_separator()  # Einen Strich ziehen
kundenoptionen.add_cascade(label="Beenden", command=root.quit)

menubar.add_cascade(label=" 2019 by. Frank Panzer")

root.config(menu=menubar)
root.mainloop()