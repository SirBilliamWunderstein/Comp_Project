-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurantdb
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `czntxqllxqpwsrgs`
--

DROP TABLE IF EXISTS `czntxqllxqpwsrgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `czntxqllxqpwsrgs` (
  `ID` int DEFAULT NULL,
  `Food` varchar(30) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Category` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `czntxqllxqpwsrgs`
--

LOCK TABLES `czntxqllxqpwsrgs` WRITE;
/*!40000 ALTER TABLE `czntxqllxqpwsrgs` DISABLE KEYS */;
INSERT INTO `czntxqllxqpwsrgs` VALUES (1,'Nachos Grande',260,'a'),(2,'Tacos Al Pastor',320,'b'),(3,'Chicken Quesadilla',340,'l'),(4,'Veggie Burrito',310,'b'),(5,'Loaded Fries With Jalapenos',230,'a'),(6,'Beef Enchiladas',190,'d'),(7,'Cheese Corn Dip',90,'a'),(8,'Spciy Bean Tacos',270,'a'),(9,'Fajita Sizzler',390,'d'),(10,'Grilled Chicken Chimichanga',430,'d'),(11,'Churros With Chocolate',220,'a'),(12,'Guacamole Bwon',200,'a'),(13,'Tres Leche Cake',250,'a'),(14,'Mexican Rice Bowl',370,'l'),(15,'Lime Margarita Mocktail',180,'a'),(16,'Taco Platter',420,'a'),(17,'Refried Bean Wrap',260,'a'),(18,'Corn Elote',210,'a');
/*!40000 ALTER TABLE `czntxqllxqpwsrgs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-06 11:59:33
