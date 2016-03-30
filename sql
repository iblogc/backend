-- MySQL dump 10.13  Distrib 5.7.11, for Linux (x86_64)
--
-- Host: localhost    Database: LeJuDBv11
-- ------------------------------------------------------
-- Server version	5.7.11

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
-- Table structure for table `accounts_account`
--

DROP TABLE IF EXISTS `accounts_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `security` varchar(50) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_account`
--

LOCK TABLES `accounts_account` WRITE;
/*!40000 ALTER TABLE `accounts_account` DISABLE KEYS */;
INSERT INTO `accounts_account` VALUES (1,'1b9ff5730ed3ba813d10575ea448fe693436f9e0','2016-03-28 06:10:10.377343','admin','14841787@qq.com','AmA5iMbGkS',0,0,0,1,1),(2,'d1acd51ceeeb116ea69f9e3cfdfbceedef44a98a','2016-03-28 06:32:45.256131','test','1234@qq.com','121212333',0,0,0,0,0);
/*!40000 ALTER TABLE `accounts_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_accountadmin`
--

DROP TABLE IF EXISTS `accounts_accountadmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_accountadmin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` varchar(20) NOT NULL,
  `realname` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `accounts_accountadmin_84566833` (`role_id`),
  CONSTRAINT `accounts_accoun_role_id_b83da25d_fk_accounts_accountadminrole_id` FOREIGN KEY (`role_id`) REFERENCES `accounts_accountadminrole` (`id`),
  CONSTRAINT `accounts_accountadmin_user_id_912ee011_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accountadmin`
--

LOCK TABLES `accounts_accountadmin` WRITE;
/*!40000 ALTER TABLE `accounts_accountadmin` DISABLE KEYS */;
INSERT INTO `accounts_accountadmin` VALUES (1,'10000','高','',1,NULL,2);
/*!40000 ALTER TABLE `accounts_accountadmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_accountadmindepartment`
--

DROP TABLE IF EXISTS `accounts_accountadmindepartment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_accountadmindepartment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accountadmindepartment`
--

LOCK TABLES `accounts_accountadmindepartment` WRITE;
/*!40000 ALTER TABLE `accounts_accountadmindepartment` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_accountadmindepartment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_accountadminrole`
--

DROP TABLE IF EXISTS `accounts_accountadminrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_accountadminrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `permission` varchar(1000) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accountadminrole`
--

LOCK TABLES `accounts_accountadminrole` WRITE;
/*!40000 ALTER TABLE `accounts_accountadminrole` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_accountadminrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_accountlog`
--

DROP TABLE IF EXISTS `accounts_accountlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_accountlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action` varchar(100) NOT NULL,
  `url` varchar(1000) NOT NULL,
  `request` longtext NOT NULL,
  `response` longtext NOT NULL,
  `ip_address` varchar(100) NOT NULL,
  `create_time` int(11) NOT NULL,
  `account_id_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_accountlo_account_id_id_1dea5e01_fk_accounts_account_id` (`account_id_id`),
  CONSTRAINT `accounts_accountlo_account_id_id_1dea5e01_fk_accounts_account_id` FOREIGN KEY (`account_id_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accountlog`
--

LOCK TABLES `accounts_accountlog` WRITE;
/*!40000 ALTER TABLE `accounts_accountlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_accountlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attachments_attachment`
--

DROP TABLE IF EXISTS `attachments_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attachments_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `file_name` varchar(200) NOT NULL,
  `extension` varchar(10) NOT NULL,
  `size` varchar(10) NOT NULL,
  `path` varchar(300) NOT NULL,
  `width` double NOT NULL,
  `height` double NOT NULL,
  `create_time` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `attachments_attachment_user_id_05d5a39f_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `attachments_attachment_user_id_05d5a39f_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachments_attachment`
--

LOCK TABLES `attachments_attachment` WRITE;
/*!40000 ALTER TABLE `attachments_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `attachments_attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add account',6,'add_account'),(17,'Can change account',6,'change_account'),(18,'Can delete account',6,'delete_account'),(19,'Can add account log',7,'add_accountlog'),(20,'Can change account log',7,'change_accountlog'),(21,'Can delete account log',7,'delete_accountlog'),(22,'Can add account admin',8,'add_accountadmin'),(23,'Can change account admin',8,'change_accountadmin'),(24,'Can delete account admin',8,'delete_accountadmin'),(25,'Can add account admin role',9,'add_accountadminrole'),(26,'Can change account admin role',9,'change_accountadminrole'),(27,'Can delete account admin role',9,'delete_accountadminrole'),(28,'Can add account admin department',10,'add_accountadmindepartment'),(29,'Can change account admin department',10,'change_accountadmindepartment'),(30,'Can delete account admin department',10,'delete_accountadmindepartment'),(31,'Can add attachment',11,'add_attachment'),(32,'Can change attachment',11,'change_attachment'),(33,'Can delete attachment',11,'delete_attachment'),(34,'Can add company',12,'add_company'),(35,'Can change company',12,'change_company'),(36,'Can delete company',12,'delete_company'),(37,'Can add company examine',13,'add_companyexamine'),(38,'Can change company examine',13,'change_companyexamine'),(39,'Can delete company examine',13,'delete_companyexamine'),(40,'Can add company license',14,'add_companylicense'),(41,'Can change company license',14,'change_companylicense'),(42,'Can delete company license',14,'delete_companylicense'),(43,'Can add company agency',15,'add_companyagency'),(44,'Can change company agency',15,'change_companyagency'),(45,'Can delete company agency',15,'delete_companyagency'),(46,'Can add product',16,'add_product'),(47,'Can change product',16,'change_product'),(48,'Can delete product',16,'delete_product'),(49,'Can add product model',17,'add_productmodel'),(50,'Can change product model',17,'change_productmodel'),(51,'Can delete product model',17,'delete_productmodel'),(52,'Can add product commodity',18,'add_productcommodity'),(53,'Can change product commodity',18,'change_productcommodity'),(54,'Can delete product commodity',18,'delete_productcommodity'),(55,'Can add product commodity goods',19,'add_productcommoditygoods'),(56,'Can change product commodity goods',19,'change_productcommoditygoods'),(57,'Can delete product commodity goods',19,'delete_productcommoditygoods'),(58,'Can add product category',20,'add_productcategory'),(59,'Can change product category',20,'change_productcategory'),(60,'Can delete product category',20,'delete_productcategory'),(61,'Can add product category attribute',21,'add_productcategoryattribute'),(62,'Can change product category attribute',21,'change_productcategoryattribute'),(63,'Can delete product category attribute',21,'delete_productcategoryattribute'),(64,'Can add product category attribute value',22,'add_productcategoryattributevalue'),(65,'Can change product category attribute value',22,'change_productcategoryattributevalue'),(66,'Can delete product category attribute value',22,'delete_productcategoryattributevalue'),(67,'Can add product category search',23,'add_productcategorysearch'),(68,'Can change product category search',23,'change_productcategorysearch'),(69,'Can delete product category search',23,'delete_productcategorysearch'),(70,'Can add product category search value',24,'add_productcategorysearchvalue'),(71,'Can change product category search value',24,'change_productcategorysearchvalue'),(72,'Can delete product category search value',24,'delete_productcategorysearchvalue'),(73,'Can add product brand',25,'add_productbrand'),(74,'Can change product brand',25,'change_productbrand'),(75,'Can delete product brand',25,'delete_productbrand'),(76,'Can add product brand series',26,'add_productbrandseries'),(77,'Can change product brand series',26,'change_productbrandseries'),(78,'Can delete product brand series',26,'delete_productbrandseries'),(79,'Can add property',27,'add_property'),(80,'Can change property',27,'change_property'),(81,'Can delete property',27,'delete_property'),(82,'Can add property profile',28,'add_propertyprofile'),(83,'Can change property profile',28,'change_propertyprofile'),(84,'Can delete property profile',28,'delete_propertyprofile'),(85,'Can add property apartment',29,'add_propertyapartment'),(86,'Can change property apartment',29,'change_propertyapartment'),(87,'Can delete property apartment',29,'delete_propertyapartment'),(88,'Can add property album',30,'add_propertyalbum'),(89,'Can change property album',30,'change_propertyalbum'),(90,'Can delete property album',30,'delete_propertyalbum'),(91,'Can add property album picture',31,'add_propertyalbumpicture'),(92,'Can change property album picture',31,'change_propertyalbumpicture'),(93,'Can delete property album picture',31,'delete_propertyalbumpicture'),(94,'Can add dictionary',32,'add_dictionary'),(95,'Can change dictionary',32,'change_dictionary'),(96,'Can delete dictionary',32,'delete_dictionary'),(97,'Can add region',33,'add_region'),(98,'Can change region',33,'change_region'),(99,'Can delete region',33,'delete_region'),(100,'Can add menu',34,'add_menu'),(101,'Can change menu',34,'change_menu'),(102,'Can delete menu',34,'delete_menu'),(103,'Can add sdk key',35,'add_sdkkey'),(104,'Can change sdk key',35,'change_sdkkey'),(105,'Can delete sdk key',35,'delete_sdkkey');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_company`
--

DROP TABLE IF EXISTS `customers_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `alias_name` varchar(200) NOT NULL,
  `province` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `zipcode` varchar(200) NOT NULL,
  `telephone` varchar(200) NOT NULL,
  `fax` varchar(200) NOT NULL,
  `website` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `license` varchar(200) NOT NULL,
  `license_thumb` varchar(300) NOT NULL,
  `logo` varchar(300) NOT NULL,
  `thumb` varchar(300) NOT NULL,
  `legal_name` varchar(300) NOT NULL,
  `legal_thumb` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `examine_id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_company_71877975` (`license`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_company`
--

LOCK TABLES `customers_company` WRITE;
/*!40000 ALTER TABLE `customers_company` DISABLE KEYS */;
INSERT INTO `customers_company` VALUES (1,'gezlife','格菱科技','杭州 浙江','西兴地铁站','1','88888888','1','1','11','7e1dfec4-f3c9-4656-9564-3f2593881ace','1','1','1','1','1',1,1,1,1,1),(2,'hzgl','杭州格林','西兴 杭州','新东方科技','1','66','1','1','1','8ae632b9-8e70-42d1-9c1b-bdcc9920083f','1','1','1','1','1',1,1,1,1,1);
/*!40000 ALTER TABLE `customers_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_companyagency`
--

DROP TABLE IF EXISTS `customers_companyagency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers_companyagency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `agency_company_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_companyagency`
--

LOCK TABLES `customers_companyagency` WRITE;
/*!40000 ALTER TABLE `customers_companyagency` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers_companyagency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_companyexamine`
--

DROP TABLE IF EXISTS `customers_companyexamine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers_companyexamine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `desciprtion` varchar(500) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_companyexamine_user_id_ec3e0e67_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `customers_companyexamine_user_id_ec3e0e67_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_companyexamine`
--

LOCK TABLES `customers_companyexamine` WRITE;
/*!40000 ALTER TABLE `customers_companyexamine` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers_companyexamine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_companylicense`
--

DROP TABLE IF EXISTS `customers_companylicense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers_companylicense` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_key` varchar(64) NOT NULL,
  `license_key` varchar(128) NOT NULL,
  `communication` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customers_companylic_company_id_0f785478_fk_customers_company_id` (`company_id`),
  CONSTRAINT `customers_companylic_company_id_0f785478_fk_customers_company_id` FOREIGN KEY (`company_id`) REFERENCES `customers_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_companylicense`
--

LOCK TABLES `customers_companylicense` WRITE;
/*!40000 ALTER TABLE `customers_companylicense` DISABLE KEYS */;
INSERT INTO `customers_companylicense` VALUES (1,'1','7e1dfec4-f3c9-4656-9564-3f2593881ace',1,1,1450063692,1450063692,1),(2,'1','2dd6ab26-c3df-4e6d-bb81-e06f5fdb4f47',1,1,1450063692,1450063692,2);
/*!40000 ALTER TABLE `customers_companylicense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-03-28 06:12:56.264980','2','test',1,'Added.',6,1),(2,'2016-03-28 06:16:42.863876','2','test',2,'No fields changed.',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','account'),(8,'accounts','accountadmin'),(10,'accounts','accountadmindepartment'),(9,'accounts','accountadminrole'),(7,'accounts','accountlog'),(1,'admin','logentry'),(11,'attachments','attachment'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(12,'customers','company'),(15,'customers','companyagency'),(13,'customers','companyexamine'),(14,'customers','companylicense'),(16,'products','product'),(25,'products','productbrand'),(26,'products','productbrandseries'),(20,'products','productcategory'),(21,'products','productcategoryattribute'),(22,'products','productcategoryattributevalue'),(23,'products','productcategorysearch'),(24,'products','productcategorysearchvalue'),(18,'products','productcommodity'),(19,'products','productcommoditygoods'),(17,'products','productmodel'),(27,'property','property'),(30,'property','propertyalbum'),(31,'property','propertyalbumpicture'),(29,'property','propertyapartment'),(28,'property','propertyprofile'),(35,'sdk','sdkkey'),(5,'sessions','session'),(32,'system','dictionary'),(34,'system','menu'),(33,'system','region');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2016-03-28 06:03:03.277088'),(2,'accounts','0002_account_is_superuser','2016-03-28 06:03:03.297871'),(3,'contenttypes','0001_initial','2016-03-28 06:03:03.308338'),(4,'admin','0001_initial','2016-03-28 06:03:03.338858'),(5,'admin','0002_logentry_remove_auto_add','2016-03-28 06:03:03.365001'),(6,'attachments','0001_initial','2016-03-28 06:03:03.434650'),(7,'contenttypes','0002_remove_content_type_name','2016-03-28 06:03:03.484674'),(8,'auth','0001_initial','2016-03-28 06:03:03.581202'),(9,'auth','0002_alter_permission_name_max_length','2016-03-28 06:03:03.610710'),(10,'auth','0003_alter_user_email_max_length','2016-03-28 06:03:03.630007'),(11,'auth','0004_alter_user_username_opts','2016-03-28 06:03:03.651557'),(12,'auth','0005_alter_user_last_login_null','2016-03-28 06:03:03.673410'),(13,'auth','0006_require_contenttypes_0002','2016-03-28 06:03:03.674862'),(14,'auth','0007_alter_validators_add_error_messages','2016-03-28 06:03:03.696267'),(15,'customers','0001_initial','2016-03-28 06:03:03.922038'),(16,'products','0001_initial','2016-03-28 06:03:04.136550'),(17,'property','0001_initial','2016-03-28 06:03:04.224143'),(18,'sdk','0001_initial','2016-03-28 06:03:04.237814'),(19,'sessions','0001_initial','2016-03-28 06:03:04.259173'),(20,'system','0001_initial','2016-03-28 06:03:04.303558'),(21,'products','0002_auto_20160328_0916','2016-03-28 09:17:02.495091'),(22,'products','0003_auto_20160329_0236','2016-03-29 02:36:41.906453'),(23,'products','0004_auto_20160329_0240','2016-03-29 02:40:28.825204');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_product_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `series_id` int(11) DEFAULT NULL,
  `product_no` varchar(200) NOT NULL,
  `attr_val` varchar(100) NOT NULL,
  `rule_val` varchar(100) NOT NULL,
  `is_ornament` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `args` longtext NOT NULL,
  `remark` longtext NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_category_id_9b594869_uniq` (`category_id`),
  KEY `products_product_447d3092` (`company_id`),
  KEY `products_product_brand_id_3e2e8fd1_uniq` (`brand_id`),
  KEY `products_product_series_id_7d8970b3_uniq` (`series_id`),
  CONSTRAINT `products_pr_series_id_7d8970b3_fk_products_productbrandseries_id` FOREIGN KEY (`series_id`) REFERENCES `products_productbrandseries` (`id`),
  CONSTRAINT `products_pro_category_id_9b594869_fk_products_productcategory_id` FOREIGN KEY (`category_id`) REFERENCES `products_productcategory` (`id`),
  CONSTRAINT `products_product_brand_id_3e2e8fd1_fk_products_productbrand_id` FOREIGN KEY (`brand_id`) REFERENCES `products_productbrand` (`id`),
  CONSTRAINT `products_product_company_id_58565ec8_fk_customers_company_id` FOREIGN KEY (`company_id`) REFERENCES `customers_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=258 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (190,29,'iioio',103,1,1,'1453455258405','11428,12246,13762,29195,1281:,','1430,25,',0,1,1453455272,1453455272,'{\"9\": \"9\", \"8\": \"8\", \"7\": \"7\"}','ioioi',1),(191,28,'gfgf',236,1,2,'1453451056830','11428,12246,13762,29195,1281:,','1430,25,',0,1,1453451068,1453451068,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(192,30,'tttt',74,1,1,'1453517696784','11428,12246,13762,29195,25,1281:,','1431,25,',0,1,1453704234,1453704234,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(193,31,'77',220,1,1,'1453876437860','11428,12246,13762,29195,25,1281:,','1432,25,',0,1,1453877250,1453877250,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(194,1,'布艺床',219,1,2,'CPcjbhN1','11428,12246,13762,29195,1281:,','1433,25,',0,1,1452997263,1452997263,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(195,2,'不仅以出生地',219,1,1,'CPcjbhN2','11428,12246,13762,29195,1281:,','1434,25,',0,1,1452997329,1452997329,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(196,3,'通过的',235,2,1,'CPcjbhN3','11428,12246,13762,29195,1281:,','1435,25,',0,1,1453082340,1453082340,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(197,4,'去无人色鬼',235,1,1,'CPcjbhN4','11428,12246,13762,29195,1281:,','1436,25,',0,1,1452997554,1452997554,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(198,5,'测试',114,2,3,'CPcjbhN5','11428,12246,13762,29195,1281:a,','1437,25,',0,1,1453270282,1453270282,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(199,6,'布艺床',219,1,2,'CPcjbhN6','11428,12246,13762,29195,1281:,','1438,25,',0,1,1453270282,1453270282,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(200,7,'测试22',76,2,3,'CPcjbhN7','11428,12246,13762,29195,1281:2,','1439,25,',0,1,1453270282,1453270282,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(201,8,'yuuu',279,1,1,'CPcjbhN8','11428,12246,13762,29195,25,1281:uyuyu,','1440,25,',0,1,1452733339,1452733339,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(202,9,'hh',279,1,1,'CPcjbhN9','11428,12246,13762,29195,1281:,','1441,25,',0,1,1453022114,1453022114,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(203,10,'布艺床',219,1,1,'CPcjbhN3','11428,12246,13762,29195,1281:,','1442,25,',0,1,1452752809,1452752809,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(204,12,'床头柜',235,2,1,'CPcjbhN12','11428,12246,13762,29195,1281:,','1443,25,',0,1,1453030883,1453030883,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(205,13,'沙发',357,2,2,'CPcjbhN13','11428,12246,13762,29195,1281:,','1444,25,',0,1,1453031084,1453031084,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(206,14,'45',103,1,1,'CPcjbhN7','11428,12246,13762,29195,25,1281:,','1445,25,',0,1,1452936432,1452936432,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(207,11,'布艺床',277,1,2,'CPcjbhN11','11428,12246,13762,29195,25,1281:,','1446,25,',0,1,1453030050,1453030050,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(208,15,'123',101,2,1,'CPcjbhN15','11428,12246,13762,29195,1281:,','1447,25,',0,1,1453080856,1453080856,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(209,16,'song',281,1,2,'CPcjbhN16','11428,12246,13762,29195,25,1281:,','1448,25,',0,1,1453081806,1453081806,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(210,17,'songtest',236,1,1,'CPcjbhN17','11428,12246,13762,29195,25,1281:12,','1449,25,',0,1,1453087955,1453087955,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(211,18,'cp1',236,1,2,'CPcjbhN1','11428,12246,13762,29195,1281:,','1450,25,',0,1,1453084928,1453084928,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(212,19,'test',220,1,2,'CPcjbhN19','11428,12246,13762,29195,25,1281:,','1451,25,',0,1,1453108644,1453108644,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(213,20,'cp3',74,1,2,'CPcjbhN3','11428,12246,13762,29195,25,1281:,','1452,25,',0,1,1453105250,1453105250,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(214,21,'cp4',103,2,3,'CPcjbhN4','11428,12246,13762,29195,25,1281:,','1453,25,',0,1,1453166614,1453166614,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(215,22,'cp5',84,1,1,'CPcjbhN5','11429,12247,13763,29196,28,1281:hhhhhhh,','1454,25,',0,1,1453181564,1453181564,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(216,23,'cp6',235,2,3,'CPcjbhN6','11428,12246,13762,29195,1281:,','1455,25,',0,1,1453169843,1453169843,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(217,24,'cp7',234,1,2,'CPcjbhN7','11428,12246,13762,29195,25,1281:,','1456,25,',0,1,1453181810,1453181810,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(218,25,'456',219,2,1,'CPcjbhN8','11428,12246,13762,29195,1281:,','1457,25,',0,1,1453188338,1453188338,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(219,26,'rrrr',235,2,3,'CPcjbhN9','11428,12246,13762,29195,1281:,','1458,25,',0,1,1453361386,1453361386,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(220,27,'ggg',220,2,3,'1453361601203','11428,12246,13762,29195,25,1281:,','1459,25,',0,1,1453361813,1453361813,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(221,32,'6',235,1,1,'1453878607658','11428,12246,13762,29195,25,1281:,','1460,25,',0,1,1453885101,1453885101,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(222,33,'yyy',235,1,1,'1453884944572','11428,12246,13762,29195,25,1281:,','1461,25,',0,1,1453885026,1453885026,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(223,34,'99999999',235,1,2,'1453885150844','11428,12246,13762,29195,25,1281:,','1462,25,',0,1,1453885232,1453885232,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(224,35,'uiii',220,1,1,'1453945661429','11428,12246,13762,29195,25,1281:,','1463,25,',0,1,1454046992,1454046992,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(225,36,'222',93,1,1,'1453949386805','11428,12246,13762,29195,1281:,','1464,25,',0,1,1453949402,1453949402,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(226,38,'qwe',418,2,3,'CPcjbhN38','11428,12246,13762,29195,1281:,','1465,25,',0,1,1453187702,1453187702,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(227,39,'轻微',418,1,2,'CPcjbhN39','11428,12246,13762,29195,1281:,','1466,25,',0,1,1453187745,1453187745,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(228,40,'111',219,2,2,'CPcjbhN40','11428,12246,13762,29195,1281:,','1467,25,',0,1,1453187784,1453187784,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(229,41,'212',219,1,2,'CPcjbhN41','11428,12246,13762,29195,25,1281:,','1468,25,',0,1,1453187964,1453187964,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(230,42,'123',418,1,2,'CPcjbhN42','11428,12246,13762,29195,1281:,','1469,25,',0,1,1453187856,1453187856,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(231,43,'轻微额',418,2,3,'CPcjbhN43','11428,12246,13762,29195,25,1281:,','1470,25,',0,1,1453187942,1453187942,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(232,44,'完美',343,1,2,'CPcjbhN44','11428,12246,13762,29195,1281:,','1471,25,',0,1,1453188038,1453188038,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(233,47,'123',219,2,1,'CPcjbhN47','11428,12246,13762,29195,1281:,','1472,25,',0,1,1453188268,1453188268,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(234,48,'不地板',93,2,1,'CPcjbhN48','11428,12246,13762,29195,1281:,','1473,25,',0,1,1453193029,1453193029,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(235,49,'uuuu',92,2,3,'CPcjbhN49','11428,12246,13762,29195,1281:,','1474,25,',0,1,1453193458,1453193458,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(236,50,'底板',102,1,1,'CPcjbhN50','11428,12246,13762,29195,25,1281:,','1475,25,',0,1,1453254290,1453254290,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(237,51,'布艺床',219,1,1,'1453428915539','11428,12246,13762,29195,25,1281:,','1476,25,',0,1,1453431158,1453431158,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(238,52,'地方机构多不好过',93,1,1,'1453430265367','11428,12246,13762,29195,25,1281:,','1477,25,',0,1,1453430294,1453430294,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(239,54,'床',219,1,1,'1453434433598','11428,12246,13762,29195,1281:,','1478,25,',0,1,1453434434,1453434434,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(240,55,'123',219,1,1,'1453441315815','11428,12246,13762,29195,25,1281:,','1479,25,',0,1,1453444294,1453444294,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(241,56,'54556446',219,2,3,'1453449351543','11428,12246,13762,29195,1281:,','1480,25,',0,1,1453449353,1453449353,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(242,58,'123',93,1,1,'1453449837148','11428,12246,13762,29195,1281:,','1481,25,',0,1,1453449845,1453449845,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(243,59,'234',93,1,2,'1453450031372','11428,12246,13762,29195,25,1281:,','1482,25,',0,1,1453515755,1453515755,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(244,60,'123123',245,2,3,'1453450740352','11428,12246,13762,29195,25,1281:,','1483,25,',0,1,1453515676,1453515676,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(245,61,'123',74,1,2,'1453450832242','11428,12246,13762,29195,25,1281:,','1484,25,',0,1,1453515708,1453515708,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(246,62,'789789',219,1,1,'1453450925567','11428,12246,13762,29195,25,1281:,','1485,25,',0,1,1453453242,1453453242,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(247,63,'qwe',219,2,3,'1453515839802','11428,12246,13762,29195,25,1281:,','1486,25,',0,1,1453874318,1453874318,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(248,65,'qwe',219,2,3,'1453860409426','11428,12246,13762,29195,1281:,','1487,25,',0,1,1453860415,1453860415,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(249,66,'qweasdzxcqwe',219,1,1,'1453861278265','11428,12246,13762,29195,1281:,','1488,25,',0,1,1453861284,1453861284,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(250,67,'地板0000',93,1,1,'1453885076309','11428,12246,13762,29195,1281:,','1489,25,',0,1,1453885082,1453885082,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(251,69,'实木沙发0000',356,2,3,'1453885349518','11428,12246,13762,29195,25,1281:,','1490,25,',0,1,1453885939,1453885939,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(252,71,'测试',74,1,2,'1453945769757','11429,12248,13765,29198,1281:,','1491,25,',0,1,1453945763,1453945763,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(253,73,'实木床333333333333333333333',226,1,1,'1453949016790','11428,12246,13762,29195,1281:,','1492,25,',0,1,1453949020,1453949020,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(254,74,'实木床44444444',226,2,3,'1453950671506','11428,12246,13762,29195,1281:,','1493,25,',0,1,1453950675,1453950675,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(255,75,'产品66666666666',69,2,3,'1454039791843','11428,12246,13762,29195,25,1281:,','1494,25,',0,1,1454047193,1454047193,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(256,37,'555',236,1,1,'1455671635303','11428,12246,13762,29195,25,1281:,','1495,25,',0,1,1455672098,1455672098,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1),(257,76,'第一个强化地板',93,1,1,'1455694748467','11429,12247,13763,29195,1281:,','1496,25,',0,1,1455694727,1455694727,'{\"7\": \"7\", \"6\": \"6\"}','ioioi',1);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productbrand`
--

DROP TABLE IF EXISTS `products_productbrand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productbrand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `name_en` varchar(100) NOT NULL,
  `alias_name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productbran_company_id_c748702c_fk_customers_company_id` (`company_id`),
  KEY `products_productbrand_user_id_ea763b30_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `products_productbran_company_id_c748702c_fk_customers_company_id` FOREIGN KEY (`company_id`) REFERENCES `customers_company` (`id`),
  CONSTRAINT `products_productbrand_user_id_ea763b30_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productbrand`
--

LOCK TABLES `products_productbrand` WRITE;
/*!40000 ALTER TABLE `products_productbrand` DISABLE KEYS */;
INSERT INTO `products_productbrand` VALUES (1,'商铺','shop','商铺111','商铺111',1,1450063829,1450063829,1,2),(2,'软件开发包','sdk','软件开发包','软件开发包',1,1450063829,1450063829,1,2),(3,'后台','manage','管理中心','中心',2,1450063829,1450063829,1,2);
/*!40000 ALTER TABLE `products_productbrand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productbrandseries`
--

DROP TABLE IF EXISTS `products_productbrandseries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productbrandseries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productbran_company_id_ad4e5b15_fk_customers_company_id` (`company_id`),
  KEY `products_productbrandser_user_id_6bb6e593_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `products_productbran_company_id_ad4e5b15_fk_customers_company_id` FOREIGN KEY (`company_id`) REFERENCES `customers_company` (`id`),
  CONSTRAINT `products_productbrandser_user_id_6bb6e593_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productbrandseries`
--

LOCK TABLES `products_productbrandseries` WRITE;
/*!40000 ALTER TABLE `products_productbrandseries` DISABLE KEYS */;
INSERT INTO `products_productbrandseries` VALUES (1,1,'商铺1号','哈哈',1,1450063829,1450063829,1,1),(2,1,'第六号商铺','嗯嗯',1,1450063829,1450063829,1,1),(3,2,'接口','呃呃',1,1450063829,1450063829,1,1),(4,1,'管理后台','数据中心',1,1450063829,1450063829,2,1);
/*!40000 ALTER TABLE `products_productbrandseries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategory`
--

DROP TABLE IF EXISTS `products_productcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `step` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `sort_id` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `parent_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `produ_parent_category_id_a15b1c75_fk_products_productcategory_id` (`parent_category_id`),
  CONSTRAINT `produ_parent_category_id_a15b1c75_fk_products_productcategory_id` FOREIGN KEY (`parent_category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=420 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategory`
--

LOCK TABLES `products_productcategory` WRITE;
/*!40000 ALTER TABLE `products_productcategory` DISABLE KEYS */;
INSERT INTO `products_productcategory` VALUES (1,'家具',1,1,0,0,0,NULL),(2,'建材',1,1,0,0,1451894118,NULL),(3,'生活用品',1,1,0,0,1451894119,NULL),(31,'大家电',2,1,0,1448441787,1451894119,3),(32,'软装饰',2,1,0,1448441787,1451894119,3),(33,'家居饰品',2,1,0,1448441787,1451894119,3),(34,'瓷砖',2,1,0,1448441787,1451894118,2),(35,'地板',2,1,0,1448441787,1451894118,2),(36,'集成吊顶',2,1,0,1448441787,1451894118,2),(37,'晾衣架/晾衣杆',2,1,0,1448441787,1451894118,2),(38,'墙纸',2,1,0,1448441787,1451894118,2),(39,'石材',2,1,0,1448441787,1451894118,2),(40,'楼梯',2,1,0,1448441787,1451894118,2),(41,'门',2,1,0,1448441787,1451894118,2),(42,'油漆类',2,1,0,1448441787,1451894118,2),(43,'灯饰照明',2,1,0,1448441787,1451894118,2),(44,'厨房用品',2,1,0,1448441787,1451894118,2),(45,'卫浴用品',2,1,0,1448441787,1451894118,2),(46,'软饰软装',2,1,0,1448441787,1451894118,2),(47,'家装五金',2,1,0,1448441787,1451894118,2),(48,'床',2,1,0,1448441787,1448441787,1),(49,'柜类',2,1,0,1448441787,1448441787,1),(50,'桌',2,1,0,1448441787,1448441787,1),(51,'案/台类',2,1,0,1448441787,1448441787,1),(52,'椅凳',2,1,0,1448441787,1448441787,1),(53,'床垫',2,1,0,1448441787,1448441787,1),(54,'沙发',2,1,0,1448441787,1448441787,1),(55,'几类',2,1,0,1448441787,1448441787,1),(56,'架类',2,1,0,1448441787,1448441787,1),(57,'屏风/花窗',2,1,0,1448441787,1448441787,1),(58,'燃气灶',3,1,0,1448442435,1451894119,31),(59,'油烟机',3,1,0,1448442435,1451894119,31),(60,'冰箱',3,1,0,1448442435,1451894119,31),(61,'空调',3,1,0,1448442435,1451894119,31),(62,'电视机',3,1,0,1448442435,1451894119,31),(63,'热水器',3,1,0,1448442435,1451894119,31),(64,'洗衣机',3,1,0,1448442435,1451894119,31),(65,'酒柜',3,1,0,1448442435,1451894119,31),(66,'音响',3,1,0,1448442435,1451894119,31),(67,'装饰摆件',3,1,0,1448442435,1451894119,32),(68,'地垫地毯',3,1,0,1448442435,1451894119,32),(69,'窗帘窗纱',3,1,0,1448442435,1451894119,32),(70,'餐桌布衣',3,1,0,1448442435,1451894119,32),(71,'防尘布艺',3,1,0,1448442435,1451894119,32),(72,'装饰画',3,1,0,1448442435,1451894119,33),(73,'梳妆镜',3,1,0,1448442435,1451894119,33),(74,'玄关镜',3,1,0,1448442435,1451894119,33),(75,'穿衣镜',3,1,0,1448442435,1451894119,33),(76,'盆栽',3,1,0,1448442435,1451894119,33),(77,'花卉',3,1,0,1448442435,1451894119,33),(78,'墙面装饰品',3,1,0,1448442435,1451894119,33),(79,'地毯',3,1,0,1448442435,1451894119,33),(80,'仿真花卉',3,1,0,1448442435,1451894119,33),(81,'工艺品',3,1,0,1448442435,1451894119,33),(82,'花瓶',3,1,0,1448442435,1451894119,33),(83,'鱼缸',3,1,0,1448442435,1451894119,33),(84,'玻化砖',3,1,0,1448442435,1451894118,34),(85,'文化砖',3,1,0,1448442435,1451894118,34),(86,'仿古砖',3,1,0,1448442435,1451894118,34),(87,'马赛克',3,1,0,1448442435,1451894118,34),(88,'抛晶砖',3,1,0,1448442435,1451894118,34),(89,'通体砖',3,1,0,1448442435,1451894118,34),(90,'微晶砖',3,1,0,1448442435,1451894118,34),(91,'釉面砖',3,1,0,1448442435,1451894118,34),(92,'地板革（PVC地板）',3,1,0,1448442435,1451894118,35),(93,'强化地板',3,1,0,1448442435,1451894118,35),(94,'强化复合地板',3,1,0,1448442435,1451894118,35),(95,'复合地板',3,1,0,1448442435,1451894118,35),(96,'实木地板',3,1,0,1448442435,1451894118,35),(97,'实木复合地板',3,1,0,1448442435,1451894118,35),(98,'特殊用途地板',3,1,0,1448442435,1451894118,35),(99,'竹地板',3,1,0,1448442435,1451894118,35),(100,'集成吊顶套餐',3,1,0,1448442435,1451894118,36),(101,'电器模块',3,1,0,1448442435,1451894118,36),(102,'扣板模块',3,1,0,1448442435,1451894118,36),(103,'配件模块',3,1,0,1448442435,1451894118,36),(104,'固定式晾衣架',3,1,0,1448442435,1451894118,37),(105,'晾衣架配件',3,1,0,1448442435,1451894118,37),(106,'升降晾衣架',3,1,0,1448442435,1451894118,37),(107,'伸缩晾衣架',3,1,0,1448442435,1451894118,37),(108,'纯纸墙纸',3,1,0,1448442435,1451894118,38),(109,'制定壁画',3,1,0,1448442435,1451894118,38),(110,'pvc墙纸',3,1,0,1448442435,1451894118,38),(111,'绒面壁纸',3,1,0,1448442435,1451894118,38),(112,'沙粒墙纸（喷砂壁纸）',3,1,0,1448442435,1451894118,38),(113,'墙布',3,1,0,1448442435,1451894118,38),(114,'壁布',3,1,0,1448442435,1451894118,38),(115,'布面墙纸',3,1,0,1448442435,1451894118,38),(116,'无纺布墙纸',3,1,0,1448442435,1451894118,38),(117,'其它材质类墙纸',3,1,0,1448442435,1451894118,38),(118,'大理石',3,1,0,1448442435,1451894118,39),(119,'花岗岩',3,1,0,1448442435,1451894118,39),(120,'石砖',3,1,0,1448442435,1451894118,39),(121,'青石砖',3,1,0,1448442435,1451894118,39),(122,'水磨石',3,1,0,1448442435,1451894118,39),(123,'楼梯踏步板',3,1,0,1448442435,1451894118,40),(124,'楼梯扶手',3,1,0,1448442435,1451894118,40),(125,'楼梯立柱',3,1,0,1448442435,1451894118,40),(126,'缩颈龙骨',3,1,0,1448442435,1451894118,40),(127,'整体楼梯',3,1,0,1448442435,1451894118,40),(128,'防火门',3,1,0,1448442435,1451894118,41),(129,'进户门',3,1,0,1448442435,1451894118,41),(130,'室内门',3,1,0,1448442435,1451894118,41),(131,'庭院门',3,1,0,1448442435,1451894118,41),(132,'移门',3,1,0,1448442435,1451894118,41),(133,'安检门',3,1,0,1448442435,1451894118,41),(134,'门附件',3,1,0,1448442435,1451894118,41),(135,'内墙乳胶漆',3,1,0,1448442435,1451894118,42),(136,'油性木器漆',3,1,0,1448442435,1451894118,42),(137,'水性木器漆',3,1,0,1448442435,1451894118,42),(138,'木蜡漆',3,1,0,1448442435,1451894118,42),(139,'外墙乳胶起',3,1,0,1448442435,1451894118,42),(140,'硅藻泥',3,1,0,1448442435,1451894118,42),(141,'特种涂料',3,1,0,1448442435,1451894118,42),(142,'室外漆',3,1,0,1448442435,1451894118,42),(143,'底漆',3,1,0,1448442435,1451894118,42),(144,'木器漆',3,1,0,1448442435,1451894118,42),(145,'乳胶漆',3,1,0,1448442435,1451894118,42),(146,'油漆套餐',3,1,0,1448442435,1451894118,42),(147,'其他',3,1,0,1448442435,1451894118,42),(148,'吊灯',3,1,0,1448442435,1451894118,43),(149,'吸顶灯',3,1,0,1448442435,1451894118,43),(150,'落地灯',3,1,0,1448442435,1451894118,43),(151,'台灯',3,1,0,1448442435,1451894118,43),(152,'壁灯',3,1,0,1448442435,1451894118,43),(153,'灯具套装',3,1,0,1448442435,1451894118,43),(154,'LED灯/光源',3,1,0,1448442435,1451894118,43),(155,'厨盆/水槽',3,1,0,1448442435,1451894118,44),(156,'水槽下水器',3,1,0,1448442435,1451894118,44),(157,'厨房龙头',3,1,0,1448442435,1451894118,44),(158,'角阀',3,1,0,1448442435,1451894118,44),(159,'厨房挂件',3,1,0,1448442435,1451894118,44),(160,'橱柜',3,1,0,1448442435,1451894118,44),(161,'微波炉支架',3,1,0,1448442435,1451894118,44),(162,'拉篮',3,1,0,1448442435,1451894118,44),(163,'置物架',3,1,0,1448442435,1451894118,44),(164,'其他厨房配件',3,1,0,1448442435,1451894118,44),(165,'浴缸',3,1,0,1448442435,1451894118,45),(166,'浴室柜',3,1,0,1448442435,1451894118,45),(167,'坐便器',3,1,0,1448442435,1451894118,45),(168,'淋浴房',3,1,0,1448442435,1451894118,45),(169,'花洒',3,1,0,1448442435,1451894118,45),(170,'卫浴龙头',3,1,0,1448442435,1451894118,45),(171,'卫浴挂件',3,1,0,1448442435,1451894118,45),(172,'地漏',3,1,0,1448442435,1451894118,45),(173,'洗脸盆',3,1,0,1448442435,1451894118,45),(174,'蹲便器',3,1,0,1448442435,1451894118,45),(175,'坐便器盖板',3,1,0,1448442435,1451894118,45),(176,'沐浴桶/沐浴盆',3,1,0,1448442435,1451894118,45),(177,'位于套装',3,1,0,1448442435,1451894118,45),(178,'浴霸',3,1,0,1448442435,1451894118,45),(179,'吊顶',3,1,0,1448442435,1451894118,45),(180,'冲水箱',3,1,0,1448442435,1451894118,45),(181,'浴巾架/毛巾架',3,1,0,1448442435,1451894118,45),(182,'面盆龙头',3,1,0,1448442435,1451894118,45),(183,'背景墙软包',3,1,0,1448442435,1451894118,46),(184,'床头套',3,1,0,1448442435,1451894118,46),(185,'工艺软包',3,1,0,1448442435,1451894118,46),(186,'天花板软包',3,1,0,1448442435,1451894118,46),(187,'开关插座',3,1,0,1448442435,1451894118,47),(188,'锁具',3,1,0,1448442435,1451894118,47),(189,'测量工具',3,1,0,1448442435,1451894118,47),(190,'门吸',3,1,0,1448442435,1451894118,47),(191,'合页',3,1,0,1448442435,1451894118,47),(192,'地漏',3,1,0,1448442435,1451894118,47),(193,'角阀',3,1,0,1448442435,1451894118,47),(194,'板材',3,1,0,1448442435,1451894118,47),(195,'硅胶',3,1,0,1448442435,1451894118,47),(196,'法兰',3,1,0,1448442435,1451894118,47),(197,'弹簧',3,1,0,1448442435,1451894118,47),(198,'铆钉',3,1,0,1448442435,1451894118,47),(199,'导轨',3,1,0,1448442435,1451894118,47),(200,'电线',3,1,0,1448442435,1451894118,47),(201,'管道',3,1,0,1448442435,1451894118,47),(202,'配电箱',3,1,0,1448442435,1451894118,47),(203,'拉手',3,1,0,1448442435,1451894118,47),(204,'接线板',3,1,0,1448442435,1451894118,47),(205,'强弱电箱',3,1,0,1448442435,1451894118,47),(206,'电线电缆',3,1,0,1448442435,1451894118,47),(207,'变压器',3,1,0,1448442435,1451894118,47),(208,'继电器',3,1,0,1448442435,1451894118,47),(209,'传感器',3,1,0,1448442435,1451894118,47),(210,'断路器',3,1,0,1448442435,1451894118,47),(211,'稳压器',3,1,0,1448442435,1451894118,47),(212,'配电箱',3,1,0,1448442435,1451894118,47),(213,'电源转换器',3,1,0,1448442435,1451894118,47),(214,'插头',3,1,0,1448442435,1451894118,47),(215,'温控器',3,1,0,1448442435,1451894118,47),(216,'节电器',3,1,0,1448442435,1451894118,47),(217,'阀',3,1,0,1448442435,1451894118,47),(218,'管材',3,1,0,1448442435,1451894118,47),(219,'布艺床',3,1,0,1448442435,1450246849,48),(220,'板式床',3,1,0,1448442435,1450246851,48),(221,'拔步床/架子床',3,1,0,1448442435,1450253952,48),(222,'板木结合床',3,1,0,1448442435,1448613217,48),(223,'充气床',3,1,0,1448442435,1448442435,48),(224,'儿童床',3,1,0,1448442435,1448442435,48),(225,'皮质床',3,1,0,1448442435,1448442435,48),(226,'实木床',3,1,0,1448442435,1448442435,48),(227,'藤艺床',3,1,0,1448442435,1448442435,48),(228,'铁艺/钢木床',3,1,0,1448442435,1448442435,48),(229,'婴儿床',3,1,0,1448442435,1448442435,48),(230,'折叠床/午休床',3,1,0,1448442435,1448442435,48),(231,'罗汉床',3,1,0,1448442435,1448442435,48),(232,'户外床',3,1,0,1448442435,1448442435,48),(233,'其他床类',3,1,0,1448442435,1448442435,48),(234,'床头柜',3,1,0,1448442435,1448442435,49),(235,'边柜',3,1,0,1448442435,1448442435,49),(236,'餐边柜',3,1,0,1448442435,1448442435,49),(237,'电视副柜',3,1,0,1448442435,1448442435,49),(238,'电视主柜',3,1,0,1448442435,1448442435,49),(239,'吊柜/壁柜',3,1,0,1448442435,1448442435,49),(240,'斗柜',3,1,0,1448442435,1448442435,49),(241,'顶箱柜',3,1,0,1448442435,1448442435,49),(242,'佛柜/佛龛',3,1,0,1448442435,1448442435,49),(243,'衣柜',3,1,0,1448442435,1448442435,49),(244,'走入式衣柜',3,1,0,1448442435,1448442435,49),(245,'茶水柜',3,1,0,1448442435,1448442435,49),(246,'酒柜',3,1,0,1448442435,1448442435,49),(247,'角柜',3,1,0,1448442435,1448442435,49),(248,'连体书桌柜',3,1,0,1448442435,1448442435,49),(249,'厅柜',3,1,0,1448442435,1448442435,49),(250,'门厅/玄关柜',3,1,0,1448442435,1448442435,49),(251,'飘窗柜',3,1,0,1448442435,1448442435,49),(252,'书柜',3,1,0,1448442435,1448442435,49),(253,'鞋柜',3,1,0,1448442435,1448442435,49),(254,'药柜',3,1,0,1448442435,1448442435,49),(255,'实验柜',3,1,0,1448442435,1448442435,49),(256,'多功能柜',3,1,0,1448442435,1449913283,49),(257,'收藏柜',3,1,0,1448442435,1448442435,49),(258,'办公柜',3,1,0,1448442435,1448442435,49),(259,'装饰柜',3,1,0,1448442435,1448442435,49),(260,'地柜',3,1,0,1448442435,1448442435,49),(261,'瓷器柜',3,1,0,1448442435,1448442435,49),(262,'户外柜',3,1,0,1448442435,1448442435,49),(263,'儿童柜类',3,1,0,1448442435,1448442435,49),(264,'儿童床头柜',3,1,0,1448442435,1448442435,49),(265,'矮柜',3,1,0,1448442435,1448442435,49),(266,'保险柜',3,1,0,1448442435,1448442435,49),(267,'文件柜',3,1,0,1448442435,1448442435,49),(268,'杂物柜',3,1,0,1448442435,1448442435,49),(269,'沙发柜',3,1,0,1448442435,1448442435,49),(270,'博古柜',3,1,0,1448442435,1448442435,49),(271,'入户柜',3,1,0,1448442435,1448442435,49),(272,'洗衣机柜',3,1,0,1448442435,1448442435,49),(273,'浴室柜',3,1,0,1448442435,1448442435,49),(274,'洗手柜',3,1,0,1448442435,1448442435,49),(275,'其他柜类',3,1,0,1448442435,1448442435,49),(276,'餐桌',3,1,0,1448442435,1448442435,50),(277,'办公桌',3,1,0,1448442435,1448442435,50),(278,'办公电脑桌',3,1,0,1448442435,1448442435,50),(279,'大班台/主管桌',3,1,0,1448442435,1448442435,50),(280,'会议桌',3,1,0,1448442435,1448442435,50),(281,'课桌',3,1,0,1448442435,1448442435,50),(282,'讲桌',3,1,0,1448442435,1448442435,50),(283,'阅览桌',3,1,0,1448442435,1448442435,50),(284,'户外桌',3,1,0,1448442435,1448442435,50),(285,'写字桌',3,1,0,1448442435,1448442435,50),(286,'根雕茶桌',3,1,0,1448442435,1448442435,50),(287,'棋桌',3,1,0,1448442435,1448442435,50),(288,'儿童桌',3,1,0,1448442435,1448442435,50),(289,'沙发桌',3,1,0,1448442435,1448442435,50),(290,'折叠桌',3,1,0,1448442435,1448442435,50),(291,'琴桌',3,1,0,1448442435,1448442435,50),(292,'台球桌',3,1,0,1448442435,1448442435,50),(293,'玄关桌',3,1,0,1448442435,1448442435,50),(294,'中堂方桌',3,1,0,1448442435,1448442435,50),(295,'餐桌椅套装',3,1,0,1448442435,1448442435,50),(296,'吧台',3,1,0,1448442435,1448442435,51),(297,'条案',3,1,0,1448442435,1448442435,51),(298,'玄关台',3,1,0,1448442435,1448442435,51),(299,'前台/接待台',3,1,0,1448442435,1448442435,51),(300,'书台',3,1,0,1448442435,1448442435,51),(301,'演讲台',3,1,0,1448442435,1448442435,51),(302,'大班台',3,1,0,1448442435,1448442435,51),(303,'中班台',3,1,0,1448442435,1448442435,51),(304,'梳妆台',3,1,0,1448442435,1448442435,51),(305,'休闲台',3,1,0,1448442435,1448442435,51),(306,'灯台',3,1,0,1448442435,1448442435,51),(307,'茶台',3,1,0,1448442435,1448442435,51),(308,'咖啡台',3,1,0,1448442435,1448442435,51),(309,'餐台',3,1,0,1448442435,1448442435,51),(310,'桌台',3,1,0,1448442435,1448442435,51),(311,'吧椅',3,1,0,1448442435,1448442435,52),(312,'贵妃椅',3,1,0,1448442435,1448442435,52),(313,'书椅',3,1,0,1448442435,1448442435,52),(314,'脚踏',3,1,0,1448442435,1448442435,52),(315,'休闲椅',3,1,0,1448442435,1448442435,52),(316,'茶椅',3,1,0,1448442435,1448442435,52),(317,'太师椅',3,1,0,1448442435,1448442435,52),(318,'琴凳',3,1,0,1448442435,1448442435,52),(319,'圈椅',3,1,0,1448442435,1448442435,52),(320,'休闲椅躺椅',3,1,0,1448442435,1448442435,52),(321,'餐椅',3,1,0,1448442435,1448442435,52),(322,'妆椅',3,1,0,1448442435,1448442435,52),(323,'梳妆椅',3,1,0,1448442435,1448442435,52),(324,'床尾凳',3,1,0,1448442435,1448442435,52),(325,'转椅',3,1,0,1448442435,1448442435,52),(326,'扶手椅',3,1,0,1448442435,1448442435,52),(327,'靠背椅',3,1,0,1448442435,1448442435,52),(328,'根雕凳子',3,1,0,1448442435,1448442435,52),(329,'摇椅',3,1,0,1448442435,1448442435,52),(330,'接待椅',3,1,0,1448442435,1448442435,52),(331,'大班椅/老板椅',3,1,0,1448442435,1448442435,52),(332,'会议椅/会客椅',3,1,0,1448442435,1448442435,52),(333,'培训椅',3,1,0,1448442435,1448442435,52),(334,'前台椅',3,1,0,1448442435,1448442435,52),(335,'休闲椅',3,1,0,1448442435,1448442435,52),(336,'公共休闲椅',3,1,0,1448442435,1450082420,52),(337,'中班椅',3,1,0,1448442435,1448442435,52),(338,'3D床垫',3,1,0,1448442435,1448442435,53),(339,'弹簧床垫',3,1,0,1448442435,1448442435,53),(340,'儿童床垫',3,1,0,1448442435,1448442435,53),(341,'复合床垫',3,1,0,1448442435,1448442435,53),(342,'海绵床垫',3,1,0,1448442435,1448442435,53),(343,'乳胶床垫',3,1,0,1448442435,1448442435,53),(344,'水床垫',3,1,0,1448442435,1448442435,53),(345,'圆床垫',3,1,0,1448442435,1448442435,53),(346,'椰棕床垫',3,1,0,1448442435,1448442435,53),(347,'棕榈床垫',3,1,0,1448442435,1448442435,53),(348,'其他床垫',3,1,0,1448442435,1448442435,53),(349,'布艺沙发',3,1,0,1448442435,1448442435,54),(350,'充气沙发',3,1,0,1448442435,1448442435,54),(351,'儿童沙发',3,1,0,1448442435,1448442435,54),(352,'贵妃椅',3,1,0,1448442435,1448442435,54),(353,'懒人沙发',3,1,0,1448442435,1448442435,54),(354,'皮艺沙发',3,1,0,1448442435,1448442435,54),(355,'皮布沙发',3,1,0,1448442435,1448442435,54),(356,'实木沙发',3,1,0,1448442435,1448442435,54),(357,'沙发床',3,1,0,1448442435,1448442435,54),(358,'铁艺沙发',3,1,0,1448442435,1448442435,54),(359,'藤/竹沙发',3,1,0,1448442435,1448442435,54),(360,'会客沙发',3,1,0,1448442435,1448442435,54),(361,'沙发配件',3,1,0,1448442435,1448442435,54),(362,'茶几',3,1,0,1448442435,1448442435,55),(363,'根雕茶几',3,1,0,1448442435,1448442435,55),(364,'角几/边几',3,1,0,1448442435,1448442435,55),(365,'炕几',3,1,0,1448442435,1448442435,55),(366,'套几',3,1,0,1448442435,1448442435,55),(367,'花几',3,1,0,1448442435,1448442435,55),(368,'壁炉架',3,1,0,1448442435,1448442435,56),(369,'书架',3,1,0,1448442435,1448442435,56),(370,'CD架',3,1,0,1448442435,1448442435,56),(371,'多宝架/博古架',3,1,0,1448442435,1448442435,56),(372,'搁板/置物架',3,1,0,1448442435,1448442435,56),(373,'格架',3,1,0,1448442435,1448442435,56),(374,'花架',3,1,0,1448442435,1448442435,56),(375,'根雕花架',3,1,0,1448442435,1448442435,56),(376,'画架',3,1,0,1448442435,1448442435,56),(377,'酒架',3,1,0,1448442435,1448442435,56),(378,'家用雨伞架',3,1,0,1448442435,1448442435,56),(379,'面盆架',3,1,0,1448442435,1448442435,56),(380,'书报架',3,1,0,1448442435,1448442435,56),(381,'鞋架',3,1,0,1448442435,1448442435,56),(382,'衣帽架',3,1,0,1448442435,1448442435,56),(383,'组合衣架',3,1,0,1448442435,1448442435,56),(384,'落地衣帽架',3,1,0,1448442435,1448442435,56),(385,'医药架',3,1,0,1448442435,1448442435,56),(386,'其他架类',3,1,0,1448442435,1448442435,56),(387,'安全套价',3,1,0,1448442435,1448442435,56),(388,'超市货架',3,1,0,1448442435,1448442435,56),(389,'仓储货架',3,1,0,1448442435,1448442435,56),(390,'促销架',3,1,0,1448442435,1448442435,56),(391,'服装货架',3,1,0,1448442435,1448442435,56),(392,'化妆品货架',3,1,0,1448442435,1448442435,56),(393,'面包架',3,1,0,1448442435,1448442435,56),(394,'内衣货架',3,1,0,1448442435,1448442435,56),(395,'水果架',3,1,0,1448442435,1448442435,56),(396,'蔬菜架',3,1,0,1448442435,1448442435,56),(397,'饰品架',3,1,0,1448442435,1448442435,56),(398,'图书音像货架',3,1,0,1448442435,1448442435,56),(399,'五金工具货架',3,1,0,1448442435,1448442435,56),(400,'鞋货架',3,1,0,1448442435,1448442435,56),(401,'眼镜货架',3,1,0,1448442435,1448442435,56),(402,'插屏',3,1,0,1448442435,1448442435,57),(403,'挂屏',3,1,0,1448442435,1448442435,57),(404,'花窗',3,1,0,1448442435,1448442435,57),(405,'折屏',3,1,0,1448442435,1448442435,57),(406,'座屏',3,1,0,1448442435,1448442435,57),(407,'护理屏风',3,1,0,1448442435,1448442435,57),(418,'test',3,0,0,1449899005,1459145549,48),(419,'test1',2,0,0,1449899034,1451894333,1);
/*!40000 ALTER TABLE `products_productcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategoryattribute`
--

DROP TABLE IF EXISTS `products_productcategoryattribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcategoryattribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `type` varchar(10) NOT NULL,
  `value` longtext NOT NULL,
  `is_search` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_pro_category_id_fb2dbf13_fk_products_productcategory_id` (`category_id`),
  CONSTRAINT `products_pro_category_id_fb2dbf13_fk_products_productcategory_id` FOREIGN KEY (`category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategoryattribute`
--

LOCK TABLES `products_productcategoryattribute` WRITE;
/*!40000 ALTER TABLE `products_productcategoryattribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcategoryattribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategoryattributevalue`
--

DROP TABLE IF EXISTS `products_productcategoryattributevalue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcategoryattributevalue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `attribute_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pr_attribute_id_86cd9698_fk_products_productcategoryattribute_id` (`attribute_id`),
  CONSTRAINT `pr_attribute_id_86cd9698_fk_products_productcategoryattribute_id` FOREIGN KEY (`attribute_id`) REFERENCES `products_productcategoryattribute` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategoryattributevalue`
--

LOCK TABLES `products_productcategoryattributevalue` WRITE;
/*!40000 ALTER TABLE `products_productcategoryattributevalue` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcategoryattributevalue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategorysearch`
--

DROP TABLE IF EXISTS `products_productcategorysearch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcategorysearch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_pro_category_id_efd66bff_fk_products_productcategory_id` (`category_id`),
  CONSTRAINT `products_pro_category_id_efd66bff_fk_products_productcategory_id` FOREIGN KEY (`category_id`) REFERENCES `products_productcategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategorysearch`
--

LOCK TABLES `products_productcategorysearch` WRITE;
/*!40000 ALTER TABLE `products_productcategorysearch` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcategorysearch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcategorysearchvalue`
--

DROP TABLE IF EXISTS `products_productcategorysearchvalue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcategorysearchvalue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `search_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_search_id_9dfd1041_fk_products_productcategorysearch_id` (`search_id`),
  CONSTRAINT `products_search_id_9dfd1041_fk_products_productcategorysearch_id` FOREIGN KEY (`search_id`) REFERENCES `products_productcategorysearch` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcategorysearchvalue`
--

LOCK TABLES `products_productcategorysearchvalue` WRITE;
/*!40000 ALTER TABLE `products_productcategorysearchvalue` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcategorysearchvalue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcommodity`
--

DROP TABLE IF EXISTS `products_productcommodity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcommodity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(500) NOT NULL,
  `name` varchar(200) NOT NULL,
  `category` varchar(500) NOT NULL,
  `brand` varchar(300) NOT NULL,
  `series` varchar(300) NOT NULL,
  `model_position` longtext NOT NULL,
  `account_limit` longtext NOT NULL,
  `company_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productcommo_product_id_9cde4513_fk_products_product_id` (`product_id`),
  CONSTRAINT `products_productcommo_product_id_9cde4513_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcommodity`
--

LOCK TABLES `products_productcommodity` WRITE;
/*!40000 ALTER TABLE `products_productcommodity` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcommodity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productcommoditygoods`
--

DROP TABLE IF EXISTS `products_productcommoditygoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productcommoditygoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `sale_title` varchar(300) NOT NULL,
  `category` varchar(500) NOT NULL,
  `brand` varchar(300) NOT NULL,
  `series` varchar(300) NOT NULL,
  `param_search` longtext NOT NULL,
  `param_full` longtext NOT NULL,
  `description` longtext NOT NULL,
  `price` double NOT NULL,
  `price_advise` double NOT NULL,
  `inventory` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `commodity_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_p_commodity_id_d3c132ce_fk_products_productcommodity_id` (`commodity_id`),
  CONSTRAINT `products_p_commodity_id_d3c132ce_fk_products_productcommodity_id` FOREIGN KEY (`commodity_id`) REFERENCES `products_productcommodity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productcommoditygoods`
--

LOCK TABLES `products_productcommoditygoods` WRITE;
/*!40000 ALTER TABLE `products_productcommoditygoods` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productcommoditygoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productmodel`
--

DROP TABLE IF EXISTS `products_productmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version_no` varchar(200) NOT NULL,
  `norms_no` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `material` varchar(100) NOT NULL,
  `norms` varchar(100) NOT NULL,
  `technics` varchar(100) NOT NULL,
  `model_path` varchar(300) NOT NULL,
  `chartlet_path` varchar(300) NOT NULL,
  `color` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_productmodel_9bea82de` (`product_id`),
  CONSTRAINT `products_productmodel_product_id_74224a69_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productmodel`
--

LOCK TABLES `products_productmodel` WRITE;
/*!40000 ALTER TABLE `products_productmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_productmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_property`
--

DROP TABLE IF EXISTS `property_property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `alias_name` varchar(200) NOT NULL,
  `sale_name` varchar(300) NOT NULL,
  `brand` varchar(200) NOT NULL,
  `key_code` varchar(50) NOT NULL,
  `approve_code` varchar(100) NOT NULL,
  `province` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `thumb` varchar(200) NOT NULL,
  `plan_area` varchar(200) NOT NULL,
  `build_area` varchar(200) NOT NULL,
  `plan_house` varchar(200) NOT NULL,
  `green_rate` varchar(200) NOT NULL,
  `cubage_rate` varchar(200) NOT NULL,
  `house` varchar(200) NOT NULL,
  `build_type` varchar(500) NOT NULL,
  `acreage` varchar(500) NOT NULL,
  `aspect` varchar(100) NOT NULL,
  `min_price` double NOT NULL,
  `max_price` double NOT NULL,
  `min_avg_price` double NOT NULL,
  `max_avg_price` double NOT NULL,
  `property_age_limit` varchar(200) NOT NULL,
  `property_type` varchar(200) NOT NULL,
  `renovation` varchar(200) NOT NULL,
  `traffic` longtext NOT NULL,
  `education` longtext NOT NULL,
  `life` longtext NOT NULL,
  `environment` longtext NOT NULL,
  `property_company` varchar(200) NOT NULL,
  `develop_company` varchar(200) NOT NULL,
  `build_date` int(11) NOT NULL,
  `complete_date` int(11) NOT NULL,
  `deliver_date` int(11) NOT NULL,
  `persell` varchar(200) NOT NULL,
  `tags` varchar(300) NOT NULL,
  `account_id` int(11) NOT NULL,
  `license` varchar(200) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_property_b068931c` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_property`
--

LOCK TABLES `property_property` WRITE;
/*!40000 ALTER TABLE `property_property` DISABLE KEYS */;
/*!40000 ALTER TABLE `property_property` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_propertyalbum`
--

DROP TABLE IF EXISTS `property_propertyalbum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property_propertyalbum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_propertyalbum`
--

LOCK TABLES `property_propertyalbum` WRITE;
/*!40000 ALTER TABLE `property_propertyalbum` DISABLE KEYS */;
/*!40000 ALTER TABLE `property_propertyalbum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_propertyalbumpicture`
--

DROP TABLE IF EXISTS `property_propertyalbumpicture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property_propertyalbumpicture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `album_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` varchar(300) NOT NULL,
  `thumb` varchar(300) NOT NULL,
  `create_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_propertyalbumpicture`
--

LOCK TABLES `property_propertyalbumpicture` WRITE;
/*!40000 ALTER TABLE `property_propertyalbumpicture` DISABLE KEYS */;
/*!40000 ALTER TABLE `property_propertyalbumpicture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_propertyapartment`
--

DROP TABLE IF EXISTS `property_propertyapartment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property_propertyapartment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `build_type` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `thumb` varchar(300) NOT NULL,
  `acreage` varchar(10) NOT NULL,
  `aspect` varchar(100) NOT NULL,
  `coordinate` varchar(1000) NOT NULL,
  `height` double NOT NULL,
  `sale_house` longtext NOT NULL,
  `room` int(11) NOT NULL,
  `hall` int(11) NOT NULL,
  `toilet` int(11) NOT NULL,
  `kitchen` int(11) NOT NULL,
  `balcony` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `property_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `property_propertyap_property_id_e6ff5be6_fk_property_property_id` (`property_id`),
  CONSTRAINT `property_propertyap_property_id_e6ff5be6_fk_property_property_id` FOREIGN KEY (`property_id`) REFERENCES `property_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_propertyapartment`
--

LOCK TABLES `property_propertyapartment` WRITE;
/*!40000 ALTER TABLE `property_propertyapartment` DISABLE KEYS */;
/*!40000 ALTER TABLE `property_propertyapartment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_propertyprofile`
--

DROP TABLE IF EXISTS `property_propertyprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property_propertyprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `profile_data` longtext NOT NULL,
  `account_id` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `property_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `property_propertypr_property_id_aecc2e02_fk_property_property_id` (`property_id`),
  CONSTRAINT `property_propertypr_property_id_aecc2e02_fk_property_property_id` FOREIGN KEY (`property_id`) REFERENCES `property_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_propertyprofile`
--

LOCK TABLES `property_propertyprofile` WRITE;
/*!40000 ALTER TABLE `property_propertyprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `property_propertyprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sdk_sdkkey`
--

DROP TABLE IF EXISTS `sdk_sdkkey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sdk_sdkkey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `domain` varchar(200) NOT NULL,
  `token` varchar(200) NOT NULL,
  `access_key` varchar(100) NOT NULL,
  `secret_key` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sdk_sdkkey`
--

LOCK TABLES `sdk_sdkkey` WRITE;
/*!40000 ALTER TABLE `sdk_sdkkey` DISABLE KEYS */;
/*!40000 ALTER TABLE `sdk_sdkkey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_dictionary`
--

DROP TABLE IF EXISTS `system_dictionary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_dictionary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `code` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `value` varchar(2000) NOT NULL,
  `status` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_dictionary`
--

LOCK TABLES `system_dictionary` WRITE;
/*!40000 ALTER TABLE `system_dictionary` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_dictionary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_menu`
--

DROP TABLE IF EXISTS `system_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `keycode` varchar(50) NOT NULL,
  `url` varchar(300) NOT NULL,
  `params` varchar(300) NOT NULL,
  `is_menu` int(11) NOT NULL,
  `sort_id` int(11) NOT NULL,
  `icon_class` varchar(100) NOT NULL,
  `style_css` varchar(300) NOT NULL,
  `status` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `parent_menu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `system_menu_parent_menu_id_bbc9b58c_fk_system_menu_id` (`parent_menu_id`),
  CONSTRAINT `system_menu_parent_menu_id_bbc9b58c_fk_system_menu_id` FOREIGN KEY (`parent_menu_id`) REFERENCES `system_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_menu`
--

LOCK TABLES `system_menu` WRITE;
/*!40000 ALTER TABLE `system_menu` DISABLE KEYS */;
INSERT INTO `system_menu` VALUES (1,'产品和模型管理','product','/product','',1,1,'fa fa-codepen','',1,1,1446554139,1447668117,NULL),(43,'产品管理','oV4tZ3R8nLx1','/product/pdt','',1,0,'','',1,2,1447308130,1449797489,1),(44,'模型管理','i1R9p1AuOyKs','/product/model','',1,0,'','',1,2,1447308141,1449797536,1),(47,'产品分类','M1Jp5NwCuL4R','/product/category','',1,0,'','',1,2,1447753106,1447753106,1);
/*!40000 ALTER TABLE `system_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_region`
--

DROP TABLE IF EXISTS `system_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sort_id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_region`
--

LOCK TABLES `system_region` WRITE;
/*!40000 ALTER TABLE `system_region` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_region` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-29 14:49:37
