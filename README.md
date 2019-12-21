# Die Autovermietung

### Python Projekt 2019
### Copyright by Frank Panzer
> Webseite https://frank-panzer.de
> E-Mail:  frank@panzer.mobi

Ich schlage vor, Sie eine virtuelle Umgebung verwenden, um den Code auszuführen
- `pyvenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

#### Kurze Info
Fahrzeuge, Kunden, Lieferanten, Rechnungen,Zweigstellen. Konten, Mitarbeiter...         
                                                                      
### Aufbau der Konsolenanwendung:               
- Übersicht über die vorhandenen Fahrzeuge                                            
- Inkl. Status                                                                      
- Neue Fahrzeuge                                                                       
- Fahrzeuge entfernen                                                                  
- Mietpreise für Fahrzeuge festlegen
- Sortierung der Fahrzeuge
- Modell
- Status
- Vorhanden/Verliehen
- Möglichkeit einen Kunden/Mitarbeiter anzulegen und/oder zu ändern
- Kundenoptionen
- Fahrzeug leihen
- Fahrzeug zurückbringen
- Fahrzeug beschädigt/zerstört
- Beim Verleih, anzeigen des Gesamtpreises für den Zeitraum
- Rechnungen für den Kunden erstellen
- Speicherung der Rechnung in der form
- Bitte an alle Rechnungsbestandteile denken !
- MySQL Datenbank
- Verhindern von Abstürzen

# MySQL-Designer
![MySQL-Designer](https://github.com/bc24/Autovermietung/blob/master/MySQL-Designer.jpg)

#Fortschrift Status

###### Menü Auflisten
--------------
- Mitarbeiter auflisten		**	läuft**
- Kunden auflisten		**läuft**
- Fahrzeuge auflisten		**läuft**
- Zweigstellen auflisten		**läuft	**

###### Menü Anlegen
------------
- Mitarbeiter anlegen		**läuft**
- Kunden anlegen			**läuft**
- Fahrzeuge anlegen		*Fehler*
- Zweigstellen anlegen		**läuft**
- Mietpreise anlegen		~~pass~~

###### Menü Entfernen
--------------
- Mitarbeiter entfernen		**läuft**
- Kunden entfernen		**läuft**
- Fahrzeuge entfernen		**läuft**
- Zweigstellen entfernen		**läuft**

###### Menü Bearbeiten
--------------- 
- Mitarbeiter bearbeiten		~~pass~~
- Kunden bearbeiten		~~pass~~
- Fahrzeuge bearbeiten		~~pass~~
- Mitpreise bearbeiten		*Fehler*

###### Kunden Optionen
---------------
- Fahrzeug Ausleihen		~~pass~~
- Fahrzeug Zurückgeben		~~pass~~
- Fahrzeug sotieren nach Status			**läuft**
- Fahrzeug sotieren nach Modell			**läuft**
- Schadensbericht einreichen		**läuft**


