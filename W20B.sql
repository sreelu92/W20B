-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: 35.222.127.166    Database: cli_social_media
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.15-MariaDB-1:10.4.15+maria~stretch

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exploits`
--

DROP TABLE IF EXISTS `exploits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exploits` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `user_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exploits_FK` (`user_id`),
  CONSTRAINT `exploits_FK` FOREIGN KEY (`user_id`) REFERENCES `hackers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exploits`
--

LOCK TABLES `exploits` WRITE;
/*!40000 ALTER TABLE `exploits` DISABLE KEYS */;
INSERT INTO `exploits` VALUES (1,'Helooo everyone from hacker J',1),(2,'Hello V',4),(3,'HELLO J',1),(4,'Hello V from J',1),(5,'greetings from F',3),(6,'greetings from A',2),(7,'greetings from V',4),(8,'helloooooooo V from J',1),(9,'Hellooooo F from J',1),(10,'heli J from bubble',6),(11,'Hi bubble from J',1),(12,'BYE FROM J',1),(13,'HIIIIIIIIIIIIIIIII',1),(14,'helo F ',1),(15,'exploit got hacked',1),(16,'last updation',1),(17,'last exploit from J',1);
/*!40000 ALTER TABLE `exploits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hackers`
--

DROP TABLE IF EXISTS `hackers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hackers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hackers_UN` (`alias`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hackers`
--

LOCK TABLES `hackers` WRITE;
/*!40000 ALTER TABLE `hackers` DISABLE KEYS */;
INSERT INTO `hackers` VALUES (1,'J@123','passwordJ'),(2,'A@123','passwordA'),(3,'F@123','passwordF'),(4,'V@123','passwordV'),(5,'Jain','jain123'),(6,'bubble','bubble123'),(7,'dany','dany123'),(8,'Adam','adam123');
/*!40000 ALTER TABLE `hackers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'cli_social_media'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-07 15:54:41
