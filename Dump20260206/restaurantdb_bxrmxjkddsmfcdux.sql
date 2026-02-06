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
-- Table structure for table `bxrmxjkddsmfcdux`
--

DROP TABLE IF EXISTS `bxrmxjkddsmfcdux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bxrmxjkddsmfcdux` (
  `ID` int DEFAULT NULL,
  `Food` varchar(30) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Category` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bxrmxjkddsmfcdux`
--

LOCK TABLES `bxrmxjkddsmfcdux` WRITE;
/*!40000 ALTER TABLE `bxrmxjkddsmfcdux` DISABLE KEYS */;
INSERT INTO `bxrmxjkddsmfcdux` VALUES (1,'Smoky Tandoori Nachos',220,'a'),(2,'Crispy Paneer Bites',250,'a'),(3,'Garlic Butter Shrimp',310,'a'),(4,'Masala Fries',180,'a'),(5,'Tomato Basil Soup',160,'a'),(6,'Butter Chicken Lasagna',420,'l'),(7,'Spicy Cottage Cheese Sizzler',390,'a'),(8,'Creamy Mushroom Risotto',410,'l'),(9,'Thai Green Curry with Rice',380,'l'),(10,'Classic BBQ Chicken Burger',320,'l'),(11,'Veggie Delight Wrap',260,'l'),(12,'Double Cheese Smash Burger',340,'l'),(13,'Crispy Fish Fillet Burger',350,'l'),(14,'Mediterranean Falafel Wrap',270,'l'),(15,'Biscoff Cheesecake Slice',230,'d'),(16,'Classic Tiramisu Jar',250,'a'),(17,'Mango Delight Sundae',190,'a'),(18,'Choclolate Brown Mousse',220,'a');
/*!40000 ALTER TABLE `bxrmxjkddsmfcdux` ENABLE KEYS */;
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
