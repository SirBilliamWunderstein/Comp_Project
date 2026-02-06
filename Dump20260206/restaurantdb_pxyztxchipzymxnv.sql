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
-- Table structure for table `pxyztxchipzymxnv`
--

DROP TABLE IF EXISTS `pxyztxchipzymxnv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pxyztxchipzymxnv` (
  `ID` int DEFAULT NULL,
  `Food` varchar(30) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Category` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pxyztxchipzymxnv`
--

LOCK TABLES `pxyztxchipzymxnv` WRITE;
/*!40000 ALTER TABLE `pxyztxchipzymxnv` DISABLE KEYS */;
INSERT INTO `pxyztxchipzymxnv` VALUES (1,'Bruschetta al Pomodoro',210,'a'),(2,'Garlic Parmesan Breadsticks',180,'a'),(3,'Margherita Pizza',390,'l'),(4,'Pasta Alfredo',420,'l'),(5,'Lasagna Bolognese',440,'l'),(6,'Risotto ai Funghi',410,'l'),(7,'Penne Arrabbiata',380,'l'),(8,'Four Cheese Pizza',420,'l'),(9,'Spaghetti Carbonara',430,'l'),(10,'Chicken Parmigiana',460,'l'),(11,'Ceasar Salad',250,'a'),(12,'Caprese Salad',270,'a'),(13,'Tiramisu',260,'a'),(14,'Expresso Shot',120,'a'),(15,'Minestrone Soup',190,'d'),(16,'Garlic Shrimp Linguinie',470,'d'),(17,'Focaccia Bread',150,'d'),(18,'Gelatio Trio',230,'d'),(19,'Espresso Shot',120,'a');
/*!40000 ALTER TABLE `pxyztxchipzymxnv` ENABLE KEYS */;
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
