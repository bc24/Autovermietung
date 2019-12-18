-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 18. Dez 2019 um 05:55
-- Server-Version: 10.4.10-MariaDB
-- PHP-Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `cbm_autovermietung`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `fahrzeug`
--

CREATE TABLE `fahrzeug` (
  `fahrzeug_id` int(11) NOT NULL,
  `marke` varchar(50) DEFAULT NULL,
  `klasse` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `kennzeichen` varchar(50) DEFAULT NULL,
  `zweigstellen_id` int(11) DEFAULT NULL,
  `fahrzeug_preis_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `fahrzeug_preis`
--

CREATE TABLE `fahrzeug_preis` (
  `fahrzeug_preis_id` int(11) NOT NULL,
  `fahrzeug_preis_netto` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kunden`
--

CREATE TABLE `kunden` (
  `kunden_id` int(11) NOT NULL,
  `nachname` varchar(50) DEFAULT NULL,
  `vorname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` int(11) DEFAULT NULL,
  `plz_id` int(11) DEFAULT NULL,
  `telefonnr` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `mitarbeiter`
--

CREATE TABLE `mitarbeiter` (
  `mitarbeiter_id` int(11) NOT NULL,
  `nachname` varchar(50) DEFAULT NULL,
  `vorname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` int(11) DEFAULT NULL,
  `plz_id` int(11) DEFAULT NULL,
  `telefonnr` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `plz_id`
--

CREATE TABLE `plz_id` (
  `plz_id` int(11) NOT NULL,
  `plz` char(5) DEFAULT NULL,
  `ort` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rechnung`
--

CREATE TABLE `rechnung` (
  `rechnung_id` int(11) NOT NULL,
  `zweigstellen_id` int(11) DEFAULT NULL,
  `kunden_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rechnung_details`
--

CREATE TABLE `rechnung_details` (
  `rechnung_id` int(11) DEFAULT NULL,
  `fahrzeug_id` int(11) DEFAULT NULL,
  `verleih_beginn` date DEFAULT NULL,
  `verleih_ende` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstelle`
--

CREATE TABLE `zweigstelle` (
  `zweigstellen_id` int(11) NOT NULL,
  `standortname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` int(11) DEFAULT NULL,
  `plz_id` int(11) DEFAULT NULL,
  `telefonnr` int(11) DEFAULT NULL,
  `steuernummer` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstelle_mitarbeiter`
--

CREATE TABLE `zweigstelle_mitarbeiter` (
  `zweigstellen_id` int(11) DEFAULT NULL,
  `mitarbeiter_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `fahrzeug`
--
ALTER TABLE `fahrzeug`
  ADD PRIMARY KEY (`fahrzeug_id`),
  ADD KEY `zweigstellen_id` (`zweigstellen_id`),
  ADD KEY `fahrzeug_preis_id` (`fahrzeug_preis_id`);

--
-- Indizes für die Tabelle `fahrzeug_preis`
--
ALTER TABLE `fahrzeug_preis`
  ADD PRIMARY KEY (`fahrzeug_preis_id`);

--
-- Indizes für die Tabelle `kunden`
--
ALTER TABLE `kunden`
  ADD PRIMARY KEY (`kunden_id`),
  ADD KEY `plz_id` (`plz_id`);

--
-- Indizes für die Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  ADD PRIMARY KEY (`mitarbeiter_id`),
  ADD KEY `plz_id` (`plz_id`);

--
-- Indizes für die Tabelle `plz_id`
--
ALTER TABLE `plz_id`
  ADD PRIMARY KEY (`plz_id`);

--
-- Indizes für die Tabelle `rechnung`
--
ALTER TABLE `rechnung`
  ADD PRIMARY KEY (`rechnung_id`),
  ADD KEY `zweigstellen_id` (`zweigstellen_id`),
  ADD KEY `kunden_id` (`kunden_id`);

--
-- Indizes für die Tabelle `rechnung_details`
--
ALTER TABLE `rechnung_details`
  ADD KEY `rechnung_id` (`rechnung_id`),
  ADD KEY `fahrzeug_id` (`fahrzeug_id`);

--
-- Indizes für die Tabelle `zweigstelle`
--
ALTER TABLE `zweigstelle`
  ADD PRIMARY KEY (`zweigstellen_id`),
  ADD KEY `plz_id` (`plz_id`);

--
-- Indizes für die Tabelle `zweigstelle_mitarbeiter`
--
ALTER TABLE `zweigstelle_mitarbeiter`
  ADD KEY `zweigstellen_id` (`zweigstellen_id`),
  ADD KEY `mitarbeiter_id` (`mitarbeiter_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `fahrzeug`
--
ALTER TABLE `fahrzeug`
  MODIFY `fahrzeug_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `fahrzeug_preis`
--
ALTER TABLE `fahrzeug_preis`
  MODIFY `fahrzeug_preis_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `kunden`
--
ALTER TABLE `kunden`
  MODIFY `kunden_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  MODIFY `mitarbeiter_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `plz_id`
--
ALTER TABLE `plz_id`
  MODIFY `plz_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `rechnung`
--
ALTER TABLE `rechnung`
  MODIFY `rechnung_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `zweigstelle`
--
ALTER TABLE `zweigstelle`
  MODIFY `zweigstellen_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `fahrzeug`
--
ALTER TABLE `fahrzeug`
  ADD CONSTRAINT `fahrzeug_ibfk_1` FOREIGN KEY (`zweigstellen_id`) REFERENCES `zweigstelle` (`zweigstellen_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fahrzeug_ibfk_2` FOREIGN KEY (`fahrzeug_preis_id`) REFERENCES `fahrzeug_preis` (`fahrzeug_preis_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `kunden`
--
ALTER TABLE `kunden`
  ADD CONSTRAINT `kunden_ibfk_1` FOREIGN KEY (`plz_id`) REFERENCES `plz_id` (`plz_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  ADD CONSTRAINT `mitarbeiter_ibfk_1` FOREIGN KEY (`plz_id`) REFERENCES `plz_id` (`plz_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `rechnung`
--
ALTER TABLE `rechnung`
  ADD CONSTRAINT `rechnung_ibfk_1` FOREIGN KEY (`zweigstellen_id`) REFERENCES `zweigstelle` (`zweigstellen_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `rechnung_ibfk_2` FOREIGN KEY (`kunden_id`) REFERENCES `kunden` (`kunden_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `rechnung_details`
--
ALTER TABLE `rechnung_details`
  ADD CONSTRAINT `rechnung_details_ibfk_1` FOREIGN KEY (`rechnung_id`) REFERENCES `rechnung` (`rechnung_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `rechnung_details_ibfk_2` FOREIGN KEY (`fahrzeug_id`) REFERENCES `fahrzeug` (`fahrzeug_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `zweigstelle`
--
ALTER TABLE `zweigstelle`
  ADD CONSTRAINT `zweigstelle_ibfk_1` FOREIGN KEY (`plz_id`) REFERENCES `plz_id` (`plz_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints der Tabelle `zweigstelle_mitarbeiter`
--
ALTER TABLE `zweigstelle_mitarbeiter`
  ADD CONSTRAINT `zweigstelle_mitarbeiter_ibfk_1` FOREIGN KEY (`zweigstellen_id`) REFERENCES `zweigstelle` (`zweigstellen_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `zweigstelle_mitarbeiter_ibfk_2` FOREIGN KEY (`mitarbeiter_id`) REFERENCES `mitarbeiter` (`mitarbeiter_id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
