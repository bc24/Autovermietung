# Die Autovermietung
### Python Projekt 2019
###### Copyright by Frank Panzer

> ####Kontakt
>
> Webseite https://frank-panzer.de | https://bremer-community.de
>
> E-Mail:  frank@panzer.mobi
                                                                    
##### Aufbau der Konsolenanwendung:
Mit diesem Python Projekt biete ich eine Konsolenanwendung zur Autovermierung an.
Folgenes kann man bis her mit der Konsolenanwendung machen.

> Auflisten
- Mitarbeiter auflisten
- Kunden auflisten
- Fahrzeuge auflisten
- Zweigstellen auflisten

> Anlegen
- Mitarbeiter anlegen
- Kunden anlegen
- Fahrzeuge anlegen
- Zweigstellen anlegen

> Entfernen
- Mitarbeiter entfernen
- Kunden entfernen
- Fahrzeuge entfernen
- Zweigstellen entfernen

> Kunden Optionen
- Fahrzeug Ausleihen
- Fahrzeug Zurückgeben
- Fahrzeug sotieren nach Status
- Fahrzeug sotieren nach Modell
- Schadensbericht einreichen

## MySQL-Designer
![MySQL-Designer](https://github.com/bc24/Autovermietung/blob/master/MySQL-Designer.jpg)

###Fortschrift Status

#### Menü Auflisten
--------------
- Mitarbeiter auflisten		**läuft**
- Kunden auflisten		**läuft**
- Fahrzeuge auflisten		**läuft**
- Zweigstellen auflisten		**läuft**

#### Menü Anlegen
------------
- Mitarbeiter anlegen		**läuft**
- Kunden anlegen			**läuft**
- Fahrzeuge anlegen		*Fehler*
- Zweigstellen anlegen		**läuft**

#### Menü Entfernen
--------------
- Mitarbeiter entfernen		**läuft**
- Kunden entfernen		**läuft**
- Fahrzeuge entfernen		**läuft**
- Zweigstellen entfernen		**läuft**

#### Menü Bearbeiten
--------------- 
- Mitarbeiter bearbeiten		*Fehler*
- Kunden bearbeiten		**läuft**
- Fahrzeuge bearbeiten		*Fehler*

#### Kunden Optionen
---------------
- Fahrzeug Ausleihen		**(Das Fahrzeug ausleihen habe ich mit etlichen Varianten gecodet, jedoch kamen bei allen nur Fehler raus. So das ich den Code wieder entfernte.)**
- Fahrzeug Zurückgeben		**läuft**
- Fahrzeug sotieren nach Status			**läuft**
- Fahrzeug sotieren nach Modell			**läuft**
- Schadensbericht einreichen		**läuft**


#### Voraussetzungen
Ich schlage vor, Sie verwenden eine virtuelle Umgebung, um den Code auszuführen

> `pyvenv venv`
>
>`source venv/bin/activate`
>
>`pip install -r requirements.txt`

#### Quellen
- Modul MySQL Connector - https://pypi.org/project/mysql-connector-python/
- Modul sys - https://docs.python.org/3/library/sys.html
- Modul os - https://docs.python.org/3/library/os.html
- Foreign Keys - https://dev.mysql.com/doc/refman/5.5/en/create-table-foreign-keys.html
- Zufall Datensaätze - https://mockaroo.com/
- Überprüfung von ein paar Funktionen - Sven Piehl
- Buch - Einstieg in Python (Rheinwerk)


##Freigabe
Die Freigabe des Projektes ist ab 23.12.2019 für alle möglich, vorher nehme ich keine änderungsvorschläge an.
Meine Pläne für das Projekt sind:
- Mehrsprchig mit Option zum auswählen (zum teil schon vorhanden, momentan jedoch auf Privat)
- Weboberfläche
- Responsive für mehrere Endgeräte
- Grafiken
- BeeWare oder Chaquopy um eine Android Version zu erschaffen