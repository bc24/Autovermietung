"""
Copyright 2019 Frank Panzer
Python Projekt - Autovermietung

Vorausgesetzt Installationen
python -m pip install mysql-connector-python


Quellen
MySQL Connector                     -   https://pypi.org/project/mysql-connector-python/
Foreign Keys                        -   https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
Zufall Datensaätze                  -   https://mockaroo.com/
Überprüfung von ein paar Funktionen -   Sven Piehl

"""
# Datenbanken Verbindung
import mysql


# Neue Fahrzeuge einfügen
def FahrzeugeAnlegen(conn, cursor):
    Fahrzeuge_Anlegen1 = input("Bitte geben Sie eine Fahrzeugmarke ein, die Sie hinzufügen wollen: ")
    Fahrzeuge_Anlegen2 = input("Bitte geben Sie eine Fahrzeugmodell ein, die Sie hinzufügen wollen: ")
    Fahrzeuge_Anlegen3 = input(
        "Bitte geben Sie an ob das Auto zu verfügung steht(1) oder Nicht zu verfügung steht(0): ")

    mycursor = DB_CBM.cursor()

    # ID für Fahrzeug wird gehollt
    res = mycursor.execute("INSERT INTO fahrzeuge (fahrzeug_id) VALUES (%s)", (Fahrzeuge_Anlegen,))
    print(res.lastinsertid)
    fzid = res.lastinsertid

    mycursor.execute("UPDATE fahrzeuge SET (fahrzeug_id) WHERE fahrzeug_id =" + fzid, )
    mycursor.execute("UPDATE fahrzeuge SET (marke) VALUES (%s)", (Fahrzeuge_Anlegen1,))
    mycursor.execute("UPDATE fahrzeuge SET (modell) VALUES (%s)", (Fahrzeuge_Anlegen2,))
    mycursor.execute("UPDATE fahrzeuge SET (status) VALUES (%s)", (Fahrzeuge_Anlegen3,))
    mycursor.execute("UPDATE fahrzeuge SET (kennzeichen) VALUES (%s)", (Fahrzeuge_Anlegen1,))
    mycursor.execute("UPDATE fahrzeuge SET (zweigstelle_id) VALUES (%s)", (Fahrzeuge_Anlegen2,))
    mycursor.execute("UPDATE fahrzeuge SET (fahrzeug_preis_id) VALUES (%s)", (Fahrzeuge_Anlegen3,))

    myresult = mycursor.fetchall()

    for x in myresult:
        print("Das sind alle Fahrzeuge: ", x)
