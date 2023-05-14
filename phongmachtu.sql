-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: phongmachtu
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `benh_nhan`
--

DROP TABLE IF EXISTS `benh_nhan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `benh_nhan` (
  `MaBN` int(11) NOT NULL AUTO_INCREMENT,
  `TenBN` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Gtinh` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Nsinh` int(11) NOT NULL,
  `Dchi` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `NgayKham` date DEFAULT NULL,
  PRIMARY KEY (`MaBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `benh_nhan`
--

LOCK TABLES `benh_nhan` WRITE;
/*!40000 ALTER TABLE `benh_nhan` DISABLE KEYS */;
/*!40000 ALTER TABLE `benh_nhan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cach_dung`
--

DROP TABLE IF EXISTS `cach_dung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cach_dung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cachdung` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cach_dung`
--

LOCK TABLES `cach_dung` WRITE;
/*!40000 ALTER TABLE `cach_dung` DISABLE KEYS */;
/*!40000 ALTER TABLE `cach_dung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoa_don`
--

DROP TABLE IF EXISTS `hoa_don`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hoa_don` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MaBN` int(11) NOT NULL,
  `sttPhieukham` int(11) NOT NULL,
  `tienkham` int(11) NOT NULL,
  `tienthuoc` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MaBN` (`MaBN`),
  KEY `sttPhieukham` (`sttPhieukham`),
  CONSTRAINT `hoa_don_ibfk_1` FOREIGN KEY (`MaBN`) REFERENCES `benh_nhan` (`mabn`),
  CONSTRAINT `hoa_don_ibfk_2` FOREIGN KEY (`sttPhieukham`) REFERENCES `phieukb` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
/*!40000 ALTER TABLE `hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loai_benh`
--

DROP TABLE IF EXISTS `loai_benh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loai_benh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Ten` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loai_benh`
--

LOCK TABLES `loai_benh` WRITE;
/*!40000 ALTER TABLE `loai_benh` DISABLE KEYS */;
/*!40000 ALTER TABLE `loai_benh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loai_donvi`
--

DROP TABLE IF EXISTS `loai_donvi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `loai_donvi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `donvi` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loai_donvi`
--

LOCK TABLES `loai_donvi` WRITE;
/*!40000 ALTER TABLE `loai_donvi` DISABLE KEYS */;
/*!40000 ALTER TABLE `loai_donvi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhan_vien`
--

DROP TABLE IF EXISTS `nhan_vien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `nhan_vien` (
  `MaNV` int(11) NOT NULL AUTO_INCREMENT,
  `TenNV` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `NSinh` date NOT NULL,
  `Gtinh` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `DChi` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ChucVu` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `SDT` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`MaNV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhan_vien`
--

LOCK TABLES `nhan_vien` WRITE;
/*!40000 ALTER TABLE `nhan_vien` DISABLE KEYS */;
/*!40000 ALTER TABLE `nhan_vien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieukb`
--

DROP TABLE IF EXISTS `phieukb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `phieukb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NgayKham` date DEFAULT NULL,
  `MaBN` int(11) NOT NULL,
  `LoaiBenh` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `TrieuChung` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `MaThuoc` int(11) NOT NULL,
  `SoLuong` int(11) NOT NULL,
  `CachSD` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MaBN` (`MaBN`),
  KEY `MaThuoc` (`MaThuoc`),
  CONSTRAINT `phieukb_ibfk_1` FOREIGN KEY (`MaBN`) REFERENCES `benh_nhan` (`mabn`),
  CONSTRAINT `phieukb_ibfk_2` FOREIGN KEY (`MaThuoc`) REFERENCES `thuoc` (`mathuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieukb`
--

LOCK TABLES `phieukb` WRITE;
/*!40000 ALTER TABLE `phieukb` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieukb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quydinh`
--

DROP TABLE IF EXISTS `quydinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `quydinh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ten` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `quydinh` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quydinh`
--

LOCK TABLES `quydinh` WRITE;
/*!40000 ALTER TABLE `quydinh` DISABLE KEYS */;
/*!40000 ALTER TABLE `quydinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thuoc`
--

DROP TABLE IF EXISTS `thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `thuoc` (
  `MaThuoc` int(11) NOT NULL AUTO_INCREMENT,
  `TenThuoc` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Donvi` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Gia` int(11) NOT NULL,
  PRIMARY KEY (`MaThuoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thuoc`
--

LOCK TABLES `thuoc` WRITE;
/*!40000 ALTER TABLE `thuoc` DISABLE KEYS */;
/*!40000 ALTER TABLE `thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `joined_date` datetime DEFAULT NULL,
  `role` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-05 14:33:54
