CREATE DATABASE  IF NOT EXISTS `art` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `art`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: art
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `idartists` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) NOT NULL,
  `mname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) NOT NULL,
  `country` varchar(45) NOT NULL,
  `dob` int NOT NULL,
  `dod` int DEFAULT NULL,
  `a_local` enum('y','n') DEFAULT NULL,
  PRIMARY KEY (`idartists`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'Vicente',NULL,'Van Gogh','France',1853,1890,'n'),(2,'Rembrandt','Harmenszoon','van Rijn','Netherlands',1606,1669,'n'),(3,'Leonardo',NULL,'da Vinci','Italy',1452,1519,'n'),(4,'Venture','Lonzo','Coy','United Stade',1965,NULL,'y'),(5,'Deborah',NULL,'Gill','United Stade',1970,NULL,'y'),(6,'Claude',NULL,'Monet','France',1840,1926,'n'),(7,'Pablo',NULL,'Picasso','Spain',1904,1973,'n'),(8,'Michelangelo','di Lodovico','Simoni','Italy',1475,1564,'n');
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artwork`
--

DROP TABLE IF EXISTS `artwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artwork` (
  `idartwork` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `a_year` int NOT NULL,
  `period` varchar(25) NOT NULL,
  `arttype` varchar(20) NOT NULL,
  `artfile` varchar(25) NOT NULL,
  `artists_idartists` int NOT NULL,
  PRIMARY KEY (`idartwork`),
  KEY `fk_artwork_artists1_idx` (`artists_idartists`),
  CONSTRAINT `fk_artwork_artists1` FOREIGN KEY (`artists_idartists`) REFERENCES `artists` (`idartists`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artwork`
--

LOCK TABLES `artwork` WRITE;
/*!40000 ALTER TABLE `artwork` DISABLE KEYS */;
INSERT INTO `artwork` VALUES (1,'Irises',1889,'Impressionism','Oil','irises.jpg',1),(2,'The Starry Night',1889,'Post-Impressionism','Oil','starrynight.jpg',1),(3,'Sunflowers',1888,'Post-Impressionism','Oil','sunflowers.jpg',1),(4,'Night Watch',1642,'Baroque','Oil','nightwatch.jpg',2),(5,'Storm on the Sea of Galilee',1633,'Dutch Golden Age','Oil','stormgalilee.jpg',2),(6,'Head of a Woman',1508,'High Renaissance','Oil','headwoman.jpg',3),(7,'Last Supper',1498,'Renaissance','Tempra','lastsupper.jpg',3),(8,'Mona Lisa',1517,'Renaissance','Oil','monalisa.jpg',3),(9,'Hillside Stream',2005,'Modern','Oil','hillsidestream.jpg',4),(10,'Old Barn',1992,'Modern','Oil','oldbarn.jpg',4),(11,'Beach Baby',1999,'Impressionism','Oil','womengarden.jpg',5),(12,'Women in the Garden',1866,'Impressionism','Oil','womengarden.jpg',6),(13,'Old Guitarist',1904,'Modern','Oil','guitarist.jpg',7);
/*!40000 ALTER TABLE `artwork` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artwork_has_keywords`
--

DROP TABLE IF EXISTS `artwork_has_keywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artwork_has_keywords` (
  `artwork_idartwork` int NOT NULL,
  `keywords_keyword_id` int NOT NULL,
  PRIMARY KEY (`artwork_idartwork`,`keywords_keyword_id`),
  KEY `fk_artwork_has_keywords_keywords1_idx` (`keywords_keyword_id`),
  KEY `fk_artwork_has_keywords_artwork1_idx` (`artwork_idartwork`),
  CONSTRAINT `fk_artwork_has_keywords_artwork1` FOREIGN KEY (`artwork_idartwork`) REFERENCES `artwork` (`idartwork`),
  CONSTRAINT `fk_artwork_has_keywords_keywords1` FOREIGN KEY (`keywords_keyword_id`) REFERENCES `keywords` (`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artwork_has_keywords`
--

LOCK TABLES `artwork_has_keywords` WRITE;
/*!40000 ALTER TABLE `artwork_has_keywords` DISABLE KEYS */;
INSERT INTO `artwork_has_keywords` VALUES (1,1),(3,1),(12,1),(2,2),(13,2),(2,3),(9,3),(10,3),(12,3),(4,4),(6,4),(8,4),(4,5),(5,5),(6,5),(7,5),(8,5),(11,5),(12,5),(13,5),(4,6),(5,6),(5,7),(5,8),(9,8),(11,8),(5,9),(7,9),(7,10),(11,11);
/*!40000 ALTER TABLE `artwork_has_keywords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keywords`
--

DROP TABLE IF EXISTS `keywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `keywords` (
  `keyword` varchar(30) NOT NULL,
  `keyword_id` int NOT NULL,
  PRIMARY KEY (`keyword_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keywords`
--

LOCK TABLES `keywords` WRITE;
/*!40000 ALTER TABLE `keywords` DISABLE KEYS */;
INSERT INTO `keywords` VALUES ('flower',1),('blue',2),('landscape',3),('girl',4),('people',5),('battle',6),('boat',7),('water',8),('Christ',9),('food',10),('baby',11);
/*!40000 ALTER TABLE `keywords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'art'
--

--
-- Dumping routines for database 'art'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-18 11:52:16
