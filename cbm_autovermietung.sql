-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 11. Dez 2019 um 15:06
-- Server-Version: 10.4.10-MariaDB
-- PHP-Version: 7.1.33

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
-- Tabellenstruktur für Tabelle `fahrzeuge`
--

CREATE TABLE `fahrzeuge` (
  `fahrzeug_id` int(50) NOT NULL,
  `marke` varchar(50) NOT NULL,
  `modell` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `kennzeichen` varchar(50) NOT NULL,
  `zweigstelle_id` int(11) NOT NULL,
  `kfz_preis_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `fahrzeuge`
--

INSERT INTO `fahrzeuge` (`fahrzeug_id`, `marke`, `modell`, `status`, `kennzeichen`, `zweigstelle_id`, `kfz_preis_id`) VALUES
(1, 'bmw', '3er', 'da', 'hb-fp-103', 2, 250);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `kunde`
--

CREATE TABLE `kunde` (
  `kunden_id` int(50) NOT NULL,
  `vorname` varchar(50) NOT NULL,
  `nachname` varchar(50) NOT NULL,
  `strasse` varchar(100) NOT NULL,
  `hausnummer` int(50) NOT NULL,
  `plz_id` int(50) NOT NULL,
  `telefonnr` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `plz_id`
--

CREATE TABLE `plz_id` (
  `plz` int(5) NOT NULL,
  `ort` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstellen`
--

CREATE TABLE `zweigstellen` (
  `(standort_id` int(50) NOT NULL,
  `strasse` varchar(50) NOT NULL,
  `plz_id` int(50) NOT NULL,
  `hausnummer` int(10) NOT NULL,
  `telefonnr` int(50) NOT NULL,
  `steuernummer` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstellen_mitarbeiter`
--

CREATE TABLE `zweigstellen_mitarbeiter` (
  `zweigstellen_id` int(50) NOT NULL,
  `mitarbeiter_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `fahrzeuge`
--
ALTER TABLE `fahrzeuge`
  ADD PRIMARY KEY (`fahrzeug_id`),
  ADD UNIQUE KEY `kfz_preis_id` (`kfz_preis_id`),
  ADD UNIQUE KEY `kfz_preis_id_2` (`kfz_preis_id`);

--
-- Indizes für die Tabelle `kunde`
--
ALTER TABLE `kunde`
  ADD PRIMARY KEY (`kunden_id`);

--
-- Indizes für die Tabelle `plz_id`
--
ALTER TABLE `plz_id`
  ADD PRIMARY KEY (`plz`);

--
-- Indizes für die Tabelle `zweigstellen`
--
ALTER TABLE `zweigstellen`
  ADD PRIMARY KEY (`(standort_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `fahrzeuge`
--
ALTER TABLE `fahrzeuge`
  MODIFY `fahrzeug_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `kunde`
--
ALTER TABLE `kunde`
  MODIFY `kunden_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `plz_id`
--
ALTER TABLE `plz_id`
  MODIFY `plz` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `zweigstellen`
--
ALTER TABLE `zweigstellen`
  MODIFY `(standort_id` int(50) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
