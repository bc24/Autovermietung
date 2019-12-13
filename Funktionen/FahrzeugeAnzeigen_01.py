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
# Übersicht über die vorhandenen Fahrzeuge
# Menüpunkt 1
def FahrzeugeAnzeigen():
  mycursor = DB_CBM.cursor()
  mycursor.execute("SELECT * FROM fahrzeuge")
  myresult = mycursor.fetchall()
  print("SELECT * FROM fahrzeuge")
