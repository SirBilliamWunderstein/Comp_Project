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
-- Table structure for table `rlist`
--

DROP TABLE IF EXISTS `rlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rlist` (
  `IK` char(16) DEFAULT NULL,
  `Title` varchar(30) DEFAULT NULL,
  `Loc` varchar(30) DEFAULT NULL,
  `opclo` char(9) DEFAULT NULL,
  `descr` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rlist`
--

LOCK TABLES `rlist` WRITE;
/*!40000 ALTER TABLE `rlist` DISABLE KEYS */;
INSERT INTO `rlist` VALUES ('bxrmxjkddsmfcdux','Seismic Toss Cafe',NULL,NULL,'At Seismic Toss Cafe we serve a diverse variety of food ranging from Southermost cuisine of Mexico to The Highest Hills of Mont Blanc. We only serve the freshest ingredients'),('czntxqllxqpwsrgs','Los Pollos Hermanos',NULL,NULL,'In the little village where I was born, life moved at a slower pace, yet felt all the richer for it. There, my two uncles were known far and wide for their delicious cooking. They seasoned their zesty chicken using only the freshest herbs and spices. People call them Los Pollos Hermanos: the chicken brothers. Today we carry on their tradition in a manner that would make my uncles proud. The finest ingredients are brought together with love and care, then slow cooked to perfection. Yes, the old ways are still best at Los Pollos Hermanos. But don\'t take my word for it. One taste, and you\'ll know.'),('pxyztxchipzymxnv','MarioShroom',NULL,NULL,'Da Marioshroom serviamo la migliore cucina italiana, dalla pizza calda cucinata dalle mamme alla pasta Alfredo piccante che ha rovinato i migliori chef alle gare di cucina. Qui da Marioshroom facciamo tutto.');
/*!40000 ALTER TABLE `rlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-06 11:59:32
