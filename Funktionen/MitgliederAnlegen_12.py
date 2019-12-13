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
# Mitglieder Anlegen
# Menüpunkt 12
def MitgliederAnlegen():
  Mitglied_Vorname = input("Bitte geben Sie eine Vorname ein, die Sie hinzufügen wollen: ")
  Mitglied_Nachname = input("Bitte geben Sie eine Nachname ein, die Sie hinzufügen wollen: ")
  Mitglied_Strasse = input("Bitte geben Sie eine Straße ein, die Sie hinzufügen wollen: ")
  Mitglied_Hausnummer = input("Bitte geben Sie eine Hausnummer ein, die Sie hinzufügen wollen: ")
  Mitglied_Telefonnummer = input("Bitte geben Sie eien Telefonnummer ein, die Sie hinzufügen wollen: ")
  Mitglied_PLZ = input("Bitte geben Sie die PLZ ein, die Sie hinzufügen wollen: ")
  
  mycursor = DB_CBM.cursor()

  # ID für Mitglieder wird gehollt
  res = Mitglied_cursor.execute("INSERT INTO mitglieder (mitglieder_id) VALUES (%s)", (Mitglied_Anlegen1,))
  print(res.lastinsertid)
  mgid = res.lastinsertid
  
  Mitglied_cursor.execute("UPDATE mitglieder SET vorname=? WHERE mitglieder_id = ? ", (Mitglied_Vorname,  mgid))
  Mitglied_cursor.execute("UPDATE mitglieder SET nachname=? WHERE mitglieder_id = ? ", (Mitglied_Nachname,  mgid))
  Mitglied_cursor.execute("UPDATE mitglieder SET strasse=? WHERE mitglieder_id = ? ", (Mitglied_Strasse,  mgid))
  Mitglied_cursor.execute("UPDATE mitglieder SET hausnummer=? WHERE mitglieder_id = ? ", (Mitglied_Hausnummer,  mgid))
  Mitglied_cursor.execute("UPDATE mitglieder SET telefonnr=? WHERE mitglieder_id = ? ", (Mitglied_Telefonnummer,  mgid))

  
  Mitglied_cursor.execute("UPDATE mitglieder SET plz_id=(SELECT plz_id FROM plz_id WHERE plz=? limit 1) WHERE mitglieder_id = ?", (Mitglied_PLZ,  mgid))

  
#  Mitglied_cursor.execute("UPDATE mitglieder SET (fahrzeug_id) WHERE fahrzeug_id =" + fzid + (Mitglied_Anlegen0,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (vorname) VALUES (%s)", (Mitglied_Vorname,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (nachname) VALUES (%s)", (Mitglied_Nachname,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (strasse) VALUES (%s)", (Mitglied_Strasse,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (hausnummer) VALUES (%s)", (Mitglied_Hausnummer,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (plz_id) WHERE plz_id =" + fzid + (Mitglied_Anlegen0,))
#  Mitglied_cursor.execute("UPDATE mitglieder SET (telefonnr) VALUES (%s)", (Mitglied_Telefonnummer,))


  myresult = Mitglied_cursor.fetchall()

  for x in myresult:
    print("Das sind alle Mitglieder: ", x)
