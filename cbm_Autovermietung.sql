-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Erstellungszeit: 10. Dez 2019 um 11:52
-- Server-Version: 5.7.28-0ubuntu0.16.04.2
-- PHP-Version: 7.1.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `cbm_Autovermietung`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `autovermietung`
--

CREATE TABLE `autovermietung` (
  `Fahrzeuge` varchar(100) NOT NULL,
  `Lieferanten` varchar(100) NOT NULL,
  `Zweigstellen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `autovermietung`
--

INSERT INTO `autovermietung` (`Fahrzeuge`, `Lieferanten`, `Zweigstellen`) VALUES
('1', '2', '3'),
('a1', 'a2', 'a3'),
('b1', 'b2', 'b3');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Fahrzeuge`
--

CREATE TABLE `Fahrzeuge` (
  `FahrzeugID` int(50) NOT NULL,
  `Acura` text NOT NULL,
  `Alfa Romeo` text NOT NULL,
  `Aston Martin` text NOT NULL,
  `Audi` text NOT NULL,
  `Bently` text NOT NULL,
  `BMW` text NOT NULL,
  `BMW i` text NOT NULL,
  `Bugatti` text NOT NULL,
  `Buick` text NOT NULL,
  `Byton` text NOT NULL,
  `Cadillac` text NOT NULL,
  `Chevrolet` text NOT NULL,
  `Chrysler` text NOT NULL,
  `Citroen` text NOT NULL,
  `Dacia` text NOT NULL,
  `Daihatsu` text NOT NULL,
  `Dodge` text NOT NULL,
  `DS Automobiles` text NOT NULL,
  `Faraday Future` text NOT NULL,
  `Ferrari` text NOT NULL,
  `Fiat` text NOT NULL,
  `Fisker` text NOT NULL,
  `Ford` text NOT NULL,
  `GMC` text NOT NULL,
  `Holden` text NOT NULL,
  `Honda` text NOT NULL,
  `Hyundai` text NOT NULL,
  `Infiniti` text NOT NULL,
  `Isuzu` text NOT NULL,
  `Jaguar` text NOT NULL,
  `Jeep` text NOT NULL,
  `Kia` text NOT NULL,
  `Koenigsegg` text NOT NULL,
  `Lada` text NOT NULL,
  `Lamborghini` text NOT NULL,
  `Lancia` text NOT NULL,
  `Land Rover` text NOT NULL,
  `Lexus` text NOT NULL,
  `Ligier` text NOT NULL,
  `Lincoln` text NOT NULL,
  `Lotus` text NOT NULL,
  `Mahindra` text NOT NULL,
  `Maserati` text NOT NULL,
  `Maybach` text NOT NULL,
  `Mazda` text NOT NULL,
  `Mercedes Benz` text NOT NULL,
  `Mini` text NOT NULL,
  `Mitsubishi` text NOT NULL,
  `Morgan` text NOT NULL,
  `Nissan` text NOT NULL,
  `Opel` text NOT NULL,
  `Pagani` text NOT NULL,
  `Peugeot` text NOT NULL,
  `PG` text NOT NULL,
  `Piaggio` text NOT NULL,
  `Porsche` text NOT NULL,
  `Renault` text NOT NULL,
  `Rolls Royce` text NOT NULL,
  `Saab` text NOT NULL,
  `Seat` text NOT NULL,
  `Skoda` text NOT NULL,
  `Smart` text NOT NULL,
  `SsangYong` text NOT NULL,
  `StreetScooter` text NOT NULL,
  `Subaru` text NOT NULL,
  `Suzuki` text NOT NULL,
  `Tesla` text NOT NULL,
  `Toyota` text NOT NULL,
  `Triumph` text NOT NULL,
  `TVR` text NOT NULL,
  `Vauxhall` text NOT NULL,
  `Volvo` text NOT NULL,
  `VW` text NOT NULL,
  `Wiesmann` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Konten`
--

CREATE TABLE `Konten` (
  `Kundennummer` int(50) NOT NULL,
  `IBAN` int(50) NOT NULL,
  `BIC` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Kunden`
--

CREATE TABLE `Kunden` (
  `kundennummer` int(50) NOT NULL,
  `vorname` text NOT NULL,
  `nachname` text NOT NULL,
  `strasse` text NOT NULL,
  `hausnummer` int(50) NOT NULL,
  `plz` int(50) NOT NULL,
  `ort` text NOT NULL,
  `land` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Lieferanten`
--

CREATE TABLE `Lieferanten` (
  `Lieferanten ID` int(50) NOT NULL,
  `Bosch` text NOT NULL,
  `Continental` text NOT NULL,
  `Denso` text NOT NULL,
  `Magna` text NOT NULL,
  `ZF Friedrichshafen` text NOT NULL,
  `Aisin` text NOT NULL,
  `Hyundai Mobis` text NOT NULL,
  `Bridgestone-Firestone` text NOT NULL,
  `Michelin` text NOT NULL,
  `Valeo` text NOT NULL,
  `Lear` text NOT NULL,
  `Faurecia` text NOT NULL,
  `Cummins` text NOT NULL,
  `Adient` text NOT NULL,
  `Goodyear` text NOT NULL,
  `Sumitomo Electric` text NOT NULL,
  `Yazaki` text NOT NULL,
  `Mahle` text NOT NULL,
  `Aptiv` text NOT NULL,
  `Weichai Power` text NOT NULL,
  `Panasonic` text NOT NULL,
  `Toyota Boshoku` text NOT NULL,
  `Schaeffler` text NOT NULL,
  `Tenneco` text NOT NULL,
  `BorgWarner` text NOT NULL,
  `Gestamp` text NOT NULL,
  `ThyssenKrupp Automotive` text NOT NULL,
  `Yanfeng Automotive Interiors` text NOT NULL,
  `Hitachi` text NOT NULL,
  `Calsonic Kansei` text NOT NULL,
  `JTEKT` text NOT NULL,
  `Autoliv` text NOT NULL,
  `GKN` text NOT NULL,
  `Beijing Hainachuan Automotive Parts` text NOT NULL,
  `Plastic Omnium` text NOT NULL,
  `Johnson Controls` text NOT NULL,
  `TE Connectivity` text NOT NULL,
  `Joyson Electronics` text NOT NULL,
  `Flex-N-Gate` text NOT NULL,
  `Dana` text NOT NULL,
  `Hella GmbH & Co.KGaA` text NOT NULL,
  `Federal-Mogul` text NOT NULL,
  `Brose` text NOT NULL,
  `Toyoda Gosei` text NOT NULL,
  `Koito Manufacturing` text NOT NULL,
  `American Axle` text NOT NULL,
  `Benteler` text NOT NULL,
  `Samvardhana Motherson` text NOT NULL,
  `Sumitomo Rubber Industries` text NOT NULL,
  `NSK Group` text NOT NULL,
  `Mitsubishi Electric` text NOT NULL,
  `Pirelli` text NOT NULL,
  `Harman` text NOT NULL,
  `Grupo Antolin` text NOT NULL,
  `Magneti Marelli` text NOT NULL,
  `NTN` text NOT NULL,
  `Hyundai WIA` text NOT NULL,
  `Hankook Tire` text NOT NULL,
  `Eberspächer` text NOT NULL,
  `Alps Electric` text NOT NULL,
  `Delphi Technologies` text NOT NULL,
  `Dräxlmaier` text NOT NULL,
  `Freudenberg` text NOT NULL,
  `Hanon Systems` text NOT NULL,
  `Nemak` text NOT NULL,
  `Leoni` text NOT NULL,
  `Tokai Rika` text NOT NULL,
  `Mando` text NOT NULL,
  `IAC` text NOT NULL,
  `Meritor` text NOT NULL,
  `Contemporary Amperex Technology (CATL)` text NOT NULL,
  `Linamar` text NOT NULL,
  `CITIC Dicastal` text NOT NULL,
  `Yokohama Rubber` text NOT NULL,
  `NHK Spring` text NOT NULL,
  `Mann+Hummel` text NOT NULL,
  `TI Automotive` text NOT NULL,
  `NXP Semiconductors` text NOT NULL,
  `Webasto` text NOT NULL,
  `Nexteer Automotive` text NOT NULL,
  `Infineon` text NOT NULL,
  `Saint-Gobain` text NOT NULL,
  `Wabco` text NOT NULL,
  `Eaton` text NOT NULL,
  `TS Tech` text NOT NULL,
  `Stanley Electric` text NOT NULL,
  `Futaba Industrial` text NOT NULL,
  `Sumitomo Riko` text NOT NULL,
  `Cooper Standard` text NOT NULL,
  `Knorr-Bremse` text NOT NULL,
  `RenesasAsahi Glass` text NOT NULL,
  `Toyo Tire & Rubber` text NOT NULL,
  `Mitsuba Corp.` text NOT NULL,
  `CIE Automotive` text NOT NULL,
  `LG Electronics` text NOT NULL,
  `Hutchinson` text NOT NULL,
  `Garrett Motion Inc.` text NOT NULL,
  `Rheinmetall Automotive` text NOT NULL,
  `Illinois Tool Works` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Mitarbeiter`
--

CREATE TABLE `Mitarbeiter` (
  `MitarbeiterNr` int(50) NOT NULL,
  `Zweigstelle` text NOT NULL,
  `Vorname` text NOT NULL,
  `Nachname` text NOT NULL,
  `strasse` text NOT NULL,
  `hausnummer` int(50) NOT NULL,
  `plz` int(50) NOT NULL,
  `ort` text NOT NULL,
  `land` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Rechnungen`
--

CREATE TABLE `Rechnungen` (
  `Datum` date NOT NULL,
  `Kundennummer` int(50) NOT NULL,
  `Rechnungsnummer` int(50) NOT NULL,
  `Rechnungssumme` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Zweigstellen`
--

CREATE TABLE `Zweigstellen` (
  `ort` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `Zweigstellen`
--

INSERT INTO `Zweigstellen` (`ort`) VALUES
('Bremen'),
('Bremen'),
('Bremen-Nord');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `Fahrzeuge`
--
ALTER TABLE `Fahrzeuge`
  ADD PRIMARY KEY (`FahrzeugID`);

--
-- Indizes für die Tabelle `Konten`
--
ALTER TABLE `Konten`
  ADD PRIMARY KEY (`IBAN`);

--
-- Indizes für die Tabelle `Kunden`
--
ALTER TABLE `Kunden`
  ADD PRIMARY KEY (`kundennummer`);

--
-- Indizes für die Tabelle `Lieferanten`
--
ALTER TABLE `Lieferanten`
  ADD PRIMARY KEY (`Lieferanten ID`);

--
-- Indizes für die Tabelle `Mitarbeiter`
--
ALTER TABLE `Mitarbeiter`
  ADD PRIMARY KEY (`MitarbeiterNr`);

--
-- Indizes für die Tabelle `Rechnungen`
--
ALTER TABLE `Rechnungen`
  ADD PRIMARY KEY (`Rechnungsnummer`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `Fahrzeuge`
--
ALTER TABLE `Fahrzeuge`
  MODIFY `FahrzeugID` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Konten`
--
ALTER TABLE `Konten`
  MODIFY `IBAN` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Kunden`
--
ALTER TABLE `Kunden`
  MODIFY `kundennummer` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Lieferanten`
--
ALTER TABLE `Lieferanten`
  MODIFY `Lieferanten ID` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Mitarbeiter`
--
ALTER TABLE `Mitarbeiter`
  MODIFY `MitarbeiterNr` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Rechnungen`
--
ALTER TABLE `Rechnungen`
  MODIFY `Rechnungsnummer` int(50) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
