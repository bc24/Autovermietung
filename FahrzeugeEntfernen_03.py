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
# Neue Fahrzeuge entfernen
# Menüpunkt 3
def FahrzeugeEntfernen():
  Fahrzeuge_Anlegen=input("Bitte geben Sie eine Automarkte ein die Sie hinzufügen wollen: ")
  mycursor = DB_CBM.cursor()
  mycursor.execute("INSERT INTO fahrzeuge (fahrzeugmarken) VALUES (%s)", (Fahrzeuge_Anlegen),)
  myresult = mycursor.fetchall()

  for x in myresult:
    print("Das sind alle Fahrzeuge: ", x)