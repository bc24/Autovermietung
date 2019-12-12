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
# Neue Fahrzeuge einfügen
# Menüpunkt 2
def FahrzeugeAnlegen():
  Fahrzeuge_Anlegen1=input("Bitte geben Sie eine Fahrzeugmarke ein, die Sie hinzufügen wollen: ")
  Fahrzeuge_Anlegen2 = input("Bitte geben Sie eine Fahrzeugmodell ein, die Sie hinzufügen wollen: ")
  Fahrzeuge_Anlegen3 = input("Bitte geben Sie an ob das Auto zu verfügung steht(1) oder Nicht zu verfügung steht(0): ")

  mycursor = DB_CBM.cursor()

  # ID für Fahrzeug wird gehollt
  res= mycursor.execute("INSERT INTO fahrzeuge (fahrzeug_id) VALUES (%s)", (Fahrzeuge_Anlegen,))
  print(res.lastinsertid)
  fzid = res.lastinsertid

  mycursor.execute("UPDATE fahrzeuge SET (fahrzeug_id) WHERE fahrzeug_id ="+ fzid + (Fahrzeuge_Anlegen0,))
  mycursor.execute("INSERT INTO fahrzeuge (marke) VALUES (%s)", (Fahrzeuge_Anlegen1,))
  mycursor.execute("INSERT INTO fahrzeuge (modell) VALUES (%s)", (Fahrzeuge_Anlegen2,))
  mycursor.execute("INSERT INTO fahrzeuge (status) VALUES (%s)", (Fahrzeuge_Anlegen3,))
  mycursor.execute("INSERT INTO fahrzeuge (kennzeichen) VALUES (%s)", (Fahrzeuge_Anlegen1,))
  mycursor.execute("INSERT INTO fahrzeuge (zweigstelle_id) VALUES (%s)", (Fahrzeuge_Anlegen2,))
  mycursor.execute("INSERT INTO fahrzeuge (fahrzeug_preis_id) VALUES (%s)", (Fahrzeuge_Anlegen3,))

  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)
