-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 19. Dez 2019 um 23:50
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
-- Tabellenstruktur für Tabelle `ausgeliehen_details`
--

CREATE TABLE `ausgeliehen_details` (
  `ausgeliehen_id` int(11) NOT NULL,
  `kunden_id` int(11) DEFAULT NULL,
  `verleih_anfang` date DEFAULT NULL,
  `verleih_ende` date DEFAULT NULL,
  `fahrzeug_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

--
-- Daten für Tabelle `fahrzeug`
--

INSERT INTO `fahrzeug` (`fahrzeug_id`, `marke`, `klasse`, `status`, `kennzeichen`, `zweigstellen_id`, `fahrzeug_preis_id`) VALUES
(1, 'Hyundai', '1G4HR54K55U067447', '0', '337941276526984', NULL, NULL),
(2, 'GMC', 'WDDDJ7CB2BA235314', '1', '6767570007245501', NULL, NULL),
(3, 'Lexus', 'WAUDG94F15N652164', '0', '589376478750404713', NULL, NULL),
(4, 'Chevrolet', 'JM3ER2A55C0139036', '1', '676299730455950849', NULL, NULL),
(5, 'Hyundai', '3LNDL2L3XCR398991', '1', '5018556204712019028', NULL, NULL),
(6, 'Chevrolet', 'JH4CU4F47AC106155', '1', '5602227314879099', NULL, NULL),
(7, 'Chevrolet', 'SCBCP7ZA8AC301485', '1', '3558422937791107', NULL, NULL),
(8, 'Subaru', '1G6AL5SX4D0571289', '0', '3531363267574477', NULL, NULL),
(9, 'Mitsubishi', '1G4HD57208U022642', '0', '4751643427280714', NULL, NULL),
(10, 'Chevrolet', 'JN1AZ4EH8FM961174', '0', '561045437851658445', NULL, NULL),
(11, 'Saab', '1N6AD0CU2BC999873', '1', '5602214959990837', NULL, NULL),
(12, 'Dodge', '2C3CCAKG2EH645440', '1', '3550588998214003', NULL, NULL),
(13, 'Toyota', 'WVGAV3AX5EW186265', '1', '560224136608209826', NULL, NULL),
(14, 'Mercedes-Benz', 'WVWGD7AJXEW340571', '1', '4405962730068925', NULL, NULL),
(15, 'Nissan', 'WAUJT68E73A270160', '0', '3576408769968077', NULL, NULL),
(16, 'Hummer', 'JN1CV6AP6AM131749', '1', '5048371497102309', NULL, NULL),
(17, 'Subaru', '3N1BC1CP7CK320091', '0', '6331108737004604', NULL, NULL),
(18, 'Isuzu', 'WBAUN1C5XBV124800', '0', '3565835694211574', NULL, NULL),
(19, 'Chevrolet', '3VW4S7AT8EM819921', '0', '6767587899645374', NULL, NULL),
(20, 'Pontiac', '2T1BU4EE0BC236536', '0', '3530756522072602', NULL, NULL),
(21, 'Pontiac', '19UUA75627A432521', '0', '5100133035483178', NULL, NULL),
(22, 'Mercedes-Benz', '1YVHZ8BA5A5862738', '1', '3577464645502936', NULL, NULL),
(23, 'Kia', '5TFCW5F17DX681571', '0', '3585275339965258', NULL, NULL),
(24, 'Subaru', 'JHMZE2H36ES320775', '0', '5528928590988162', NULL, NULL),
(25, 'Chevrolet', '1N6AF0KY0EN247872', '0', '6762978877056954', NULL, NULL),
(26, 'Chevrolet', 'WA1CV74L69D609007', '0', '6304561119138475404', NULL, NULL),
(27, 'Mercury', '1G6DS5ED2B0880841', '0', '3562151344558114', NULL, NULL),
(28, 'Scion', '1GYS4EEJ0BR695634', '1', '3547041892530260', NULL, NULL),
(29, 'Honda', '19UUA56792A288180', '0', '5332431781852905', NULL, NULL),
(30, 'BMW', 'WBS3C9C56FP731122', '1', '4405205506152782', NULL, NULL),
(31, 'Isuzu', '3D7TT2CT9AG892600', '1', '560223920712612681', NULL, NULL),
(32, 'Hummer', 'WAUWMAFC3FN064256', '1', '3557276590957129', NULL, NULL),
(33, 'Cadillac', '1N6AD0CU6AC542420', '1', '5602256463171230', NULL, NULL),
(34, 'Mercedes-Benz', '3GYT4LEFXCG180324', '0', '5100132981972184', NULL, NULL),
(35, 'Chrysler', '2T1BURHE4EC870333', '0', '30412188389432', NULL, NULL),
(36, 'Honda', '1G6AS5S32F0735934', '0', '6304544220205663930', NULL, NULL),
(37, 'Infiniti', 'KM8JT3ACXAU115345', '1', '3553500988810200', NULL, NULL),
(38, 'Mitsubishi', '1GD022CG6CZ690380', '0', '4917245511564705', NULL, NULL),
(39, 'Ferrari', 'WAURMAFD9EN966091', '1', '4913645421983925', NULL, NULL),
(40, 'Mercedes-Benz', '2D4RN3D10AR033717', '1', '4041590051681933', NULL, NULL),
(41, 'Mazda', 'WAUAF48H19K898482', '1', '4041378600431', NULL, NULL),
(42, 'Ferrari', '1G4HP54K034781652', '0', '4175004180761010', NULL, NULL),
(43, 'Chevrolet', '3GYFNGEY0AS224747', '1', '3531412246920317', NULL, NULL),
(44, 'Pontiac', 'WAUKFBFL5DA660052', '1', '3563215406081346', NULL, NULL),
(45, 'Suzuki', 'JH4KB16697C496976', '1', '5579722850578195', NULL, NULL),
(46, 'Hummer', 'YV4940BZ2E1735567', '1', '633110994181412601', NULL, NULL),
(47, 'Volkswagen', 'WAUJF78K49N904867', '0', '3577699494508415', NULL, NULL),
(48, 'Hyundai', 'WBALZ5C59CD749574', '0', '4041376027405', NULL, NULL),
(49, 'Mitsubishi', '1G4GC5G36FF961304', '0', '3532483308894558', NULL, NULL),
(50, 'Land Rover', 'WAUGL58E85A981390', '0', '3548846848040159', NULL, NULL);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `fahrzeug_preis`
--

CREATE TABLE `fahrzeug_preis` (
  `fahrzeug_preis_id` int(11) NOT NULL,
  `fahrzeug_preis_netto` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `fahrzeug_preis`
--

INSERT INTO `fahrzeug_preis` (`fahrzeug_preis_id`, `fahrzeug_preis_netto`) VALUES
(1, 249),
(2, 260),
(3, 150),
(4, 850),
(5, 640),
(6, 146),
(7, 800),
(8, 1500),
(9, 125),
(10, 264),
(11, 164),
(12, 168),
(13, 169),
(14, 124),
(15, 246),
(16, 168),
(17, 105),
(18, 150),
(19, 160),
(20, 140),
(21, 164),
(22, 1465),
(23, 102),
(24, 164),
(25, 164),
(26, 0),
(27, 0),
(28, 0),
(29, 0),
(30, 0),
(31, 0),
(32, 0),
(33, 0),
(34, 0),
(35, 0),
(36, 0),
(37, 0),
(38, 0),
(39, 0),
(40, 0),
(41, 0),
(42, 0),
(43, 0),
(44, 0),
(45, 0),
(46, 0),
(47, 1648),
(48, 164),
(49, 145),
(50, 160);

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

--
-- Daten für Tabelle `kunden`
--

INSERT INTO `kunden` (`kunden_id`, `nachname`, `vorname`, `strasse`, `hausnummer`, `plz_id`, `telefonnr`) VALUES
(3, 'Paolone', 'Esmeralda', 'Thompson', 9, NULL, '6796597538'),
(8, 'Arnott', 'Gav', 'Stuart', 28, NULL, '6227434475'),
(9, 'Cufley', 'Matt', 'Anzinger', 7105, NULL, '9299519814'),
(10, 'Mafham', 'Nan', 'Lerdahl', 35, NULL, '5851600596'),
(15, 'Broddle', 'Ange', 'Dawn', 68245, NULL, '2392422243'),
(16, 'Gerriet', 'Solly', 'Express', 650, NULL, '7137127474'),
(17, 'Adriaan', 'Chaddie', 'Haas', 5425, NULL, '9667451943'),
(19, 'Korf', 'Leo', 'Pawling', 15073, NULL, '4649083462'),
(21, 'Firpo', 'Eldin', 'Vidon', 48, NULL, '5421111093'),
(22, 'Raybould', 'Farrel', 'Marcy', 6, NULL, '9435526452'),
(23, 'Barwack', 'Addison', 'Westerfield', 1, NULL, '1093115399'),
(24, 'Issitt', 'Lib', 'Dayton', 90, NULL, '9449537336'),
(25, 'Santos', 'Kakalina', 'Calypso', 773, NULL, '6264058613'),
(26, 'Caraher', 'Loralyn', 'North', 788, NULL, '9545610293'),
(28, 'Needham', 'Isidore', 'Fair Oaks', 172, NULL, '4687069297'),
(31, 'Maywood', 'Natalie', 'Randy', 1002, NULL, '2647718394'),
(32, 'Dibley', 'Winn', 'Buhler', 8, NULL, '8674186081'),
(33, 'Bucknall', 'Ida', 'High Crossing', 87777, NULL, '8921718014'),
(36, 'Vedenichev', 'Aurel', 'Lotheville', 9695, NULL, '6136367423'),
(39, 'Mighele', 'Wildon', 'Dakota', 7191, NULL, '1192429508'),
(40, 'De Filippis', 'Stevana', 'Ryan', 36955, NULL, '1106865818'),
(41, 'Briddle', 'Channa', 'Scofield', 6, NULL, '5535877461'),
(42, 'Stebbing', 'Ingaborg', 'Pine View', 58, NULL, '2482044636'),
(43, 'Gianelli', 'Rosanna', 'Farragut', 95219, NULL, '7183012385'),
(44, 'Sokale', 'Emmerich', 'Glacier Hill', 8949, NULL, '1411201853'),
(46, 'Jiruca', 'Cordelia', 'Carioca', 72923, NULL, '2917460214');

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

--
-- Daten für Tabelle `mitarbeiter`
--

INSERT INTO `mitarbeiter` (`mitarbeiter_id`, `nachname`, `vorname`, `strasse`, `hausnummer`, `plz_id`, `telefonnr`) VALUES
(1, 'Koubek', 'Neill', 'Summit', 196, NULL, '3898283207'),
(2, 'Demageard', 'Richmound', 'Ramsey', 6266, NULL, '7932862027'),
(3, 'Connal', 'Clementius', 'Riverside', 931, NULL, '2161213283'),
(6, 'Gooble', 'Nettle', 'Tomscot', 8343, NULL, '4349354479'),
(8, 'Dunsford', 'Daisey', 'Linden', 5, NULL, '9667978058'),
(10, 'Haslen', 'Noak', 'Darwin', 49340, NULL, '9192232298'),
(12, 'Cowope', 'Nady', 'Garrison', 6954, NULL, '3926851771'),
(17, 'Chaimson', 'Eran', 'Sutherland', 1232, NULL, '9437504005'),
(18, 'Gopsall', 'Zola', 'Sachs', 522, NULL, '8094667188'),
(20, 'McAuley', 'Ashia', '1st', 4614, NULL, '1842697287'),
(21, 'Isaacs', 'Georas', 'Dunning', 4, NULL, '5262047822'),
(22, 'Savory', 'Theresa', 'Cottonwood', 26, NULL, '3846647756'),
(23, 'Arnau', 'Moses', 'Gina', 9018, NULL, '6525036354'),
(24, 'Birmingham', 'Bunnie', 'Ronald Regan', 84, NULL, '7946632892'),
(25, 'Rubens', 'Daisie', 'Pleasure', 2, NULL, '9348859564'),
(26, 'Halmkin', 'Clo', 'Holmberg', 907, NULL, '5532858557'),
(30, 'Bess', 'Stacee', 'Glendale', 73, NULL, '3683998533'),
(32, 'Petroselli', 'Ange', 'Norway Maple', 5, NULL, '6677897491'),
(33, 'Toghill', 'Charlotta', 'Randy', 867, NULL, '4666817217'),
(34, 'Twiggins', 'Catherina', 'Gulseth', 59, NULL, '7346109269'),
(35, 'Stogill', 'Hyatt', 'Summerview', 40376, NULL, '6589160233'),
(36, 'Lorryman', 'Tildy', 'Sachs', 34661, NULL, '3559599614'),
(37, 'Mouncher', 'Bernadine', 'Anthes', 4, NULL, '5729358607'),
(38, 'Plaster', 'Alfred', 'Warrior', 1, NULL, '9637168273'),
(40, 'Golda', 'Enos', 'Donald', 4533, NULL, '2579268728'),
(41, 'Stansby', 'Gail', 'Darwin', 6, NULL, '2089471105'),
(42, 'Wintringham', 'Mikol', 'Merchant', 8, NULL, '1447065997'),
(43, 'Patsall', 'Camilla', 'Randy', 7, NULL, '2331543454'),
(44, 'Munford', 'Kristal', 'Grover', 91, NULL, '7272878926'),
(45, 'Roskam', 'Jo-anne', 'Eastwood', 73492, NULL, '5893035934'),
(47, 'Jope', 'Allayne', 'Victoria', 19, NULL, '4637850275'),
(49, 'Schiefersten', 'Georgina', 'Westport', 57, NULL, '2509215441');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `plz_id`
--

CREATE TABLE `plz_id` (
  `plz_id` int(11) NOT NULL,
  `plz` char(5) DEFAULT NULL,
  `ort` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `plz_id`
--

INSERT INTO `plz_id` (`plz_id`, `plz`, `ort`) VALUES
(1, '28201', 'Bremen'),
(2, '28777', 'Bremen'),
(3, '28199', 'Xinheng'),
(4, '28199', 'Ogaminan'),
(5, '1219', 'Mancilang'),
(6, '22111', 'Hamburg'),
(7, '33314', 'Arcachon'),
(8, '48888', 'Plaza de Caisán'),
(9, '66815', 'Sut-Khol’'),
(10, '49800', 'Butajīra'),
(11, '28757', 'Savran’'),
(12, '28199', 'Huangfang'),
(13, '78967', 'Buritis'),
(14, '79783', 'San Rafael'),
(15, '28199', 'Mafang'),
(16, '28755', 'Hengliang'),
(17, '4360', 'Karlovo'),
(18, '94631', 'Rungis'),
(19, '27201', 'Hanting'),
(20, '28259', 'Muli'),
(21, '28745', 'Mashizhai'),
(22, '28946', 'Caicara'),
(23, '373 7', 'Rudolfov'),
(24, '78430', 'Rancho Nuevo'),
(25, '6344', 'Sandayong Sur'),
(26, 'K7G', 'Gananoque'),
(27, NULL, 'Xingong'),
(28, NULL, 'Awarawar'),
(29, NULL, 'Krajan Kerjo'),
(30, NULL, 'Chaoyang'),
(31, '36372', 'Kizlyar'),
(32, 'T1M', 'Coaldale'),
(33, '4620-', 'Linhares'),
(34, NULL, 'Dongping'),
(35, NULL, 'Nouvelle France'),
(36, NULL, 'Vom'),
(37, NULL, 'Talā'),
(38, '67502', 'Blagoveshchensk'),
(39, '41355', 'Vineuil'),
(40, NULL, 'Xiangyanglu'),
(41, NULL, 'Bihać'),
(42, '1315', 'Otlja'),
(43, NULL, 'Socos'),
(44, '1307', 'Haligue'),
(45, '9025', 'Digkilaan'),
(46, '64922', 'Shebalino'),
(47, '7165', 'Villa Gesell'),
(48, NULL, 'Baalbek'),
(49, NULL, 'Teongtoda'),
(50, NULL, 'Taokeng');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rechnung`
--

CREATE TABLE `rechnung` (
  `rechnung_id` int(11) NOT NULL,
  `zweigstellen_id` int(11) DEFAULT NULL,
  `kunden_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `rechnung`
--

INSERT INTO `rechnung` (`rechnung_id`, `zweigstellen_id`, `kunden_id`) VALUES
(1, 1, 32),
(2, 2, 43),
(3, 2, 33),
(4, 1, 26);

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

--
-- Daten für Tabelle `rechnung_details`
--

INSERT INTO `rechnung_details` (`rechnung_id`, `fahrzeug_id`, `verleih_beginn`, `verleih_ende`) VALUES
(NULL, 42, '2019-12-15', '2019-12-21'),
(NULL, 27, '2019-12-01', '2019-12-31');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstelle`
--

CREATE TABLE `zweigstelle` (
  `zweigstellen_id` int(11) NOT NULL,
  `zweigstellenname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` int(11) DEFAULT NULL,
  `plz_id` int(11) DEFAULT NULL,
  `telefonnr` int(11) DEFAULT NULL,
  `steuernummer` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `zweigstelle`
--

INSERT INTO `zweigstelle` (`zweigstellen_id`, `zweigstellenname`, `strasse`, `hausnummer`, `plz_id`, `telefonnr`, `steuernummer`) VALUES
(1, 'Bremen', 'Kornstrasse', 50, 1, 468545, '457896435678'),
(2, 'Bremen-Nord', 'Kreinsloger', 103, 2, 46821685, '946255862164'),
(3, 'Bremen Flughafen', 'Flugzeugstr', 1, 4, 1234567, '25468952136');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zweigstelle_mitarbeiter`
--

CREATE TABLE `zweigstelle_mitarbeiter` (
  `zweigstellen_id` int(11) DEFAULT NULL,
  `mitarbeiter_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `zweigstelle_mitarbeiter`
--

INSERT INTO `zweigstelle_mitarbeiter` (`zweigstellen_id`, `mitarbeiter_id`) VALUES
(1, 17),
(2, 10),
(2, 1),
(3, 38);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `ausgeliehen_details`
--
ALTER TABLE `ausgeliehen_details`
  ADD PRIMARY KEY (`ausgeliehen_id`),
  ADD KEY `fahrzeug_id` (`fahrzeug_id`),
  ADD KEY `kunden_id` (`kunden_id`);

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
-- AUTO_INCREMENT für Tabelle `ausgeliehen_details`
--
ALTER TABLE `ausgeliehen_details`
  MODIFY `ausgeliehen_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `fahrzeug`
--
ALTER TABLE `fahrzeug`
  MODIFY `fahrzeug_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT für Tabelle `fahrzeug_preis`
--
ALTER TABLE `fahrzeug_preis`
  MODIFY `fahrzeug_preis_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT für Tabelle `kunden`
--
ALTER TABLE `kunden`
  MODIFY `kunden_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT für Tabelle `mitarbeiter`
--
ALTER TABLE `mitarbeiter`
  MODIFY `mitarbeiter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT für Tabelle `plz_id`
--
ALTER TABLE `plz_id`
  MODIFY `plz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT für Tabelle `rechnung`
--
ALTER TABLE `rechnung`
  MODIFY `rechnung_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT für Tabelle `zweigstelle`
--
ALTER TABLE `zweigstelle`
  MODIFY `zweigstellen_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `ausgeliehen_details`
--
ALTER TABLE `ausgeliehen_details`
  ADD CONSTRAINT `ausgeliehen_details_ibfk_1` FOREIGN KEY (`fahrzeug_id`) REFERENCES `fahrzeug` (`fahrzeug_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ausgeliehen_details_ibfk_2` FOREIGN KEY (`kunden_id`) REFERENCES `kunden` (`kunden_id`) ON DELETE SET NULL ON UPDATE CASCADE;

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
