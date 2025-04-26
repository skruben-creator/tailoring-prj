-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 26, 2025 at 04:08 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tailorshopdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookapp`
--

CREATE TABLE `bookapp` (
  `id` bigint(250) NOT NULL auto_increment,
  `name` varchar(250) NOT NULL,
  `mobile` varchar(250) NOT NULL,
  `landmark` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `pincode` varchar(250) NOT NULL,
  `buildingFloor` varchar(250) NOT NULL,
  `serviceType` varchar(250) NOT NULL,
  `appointmentDate` varchar(250) NOT NULL,
  `appointmentTime` varchar(250) NOT NULL,
  `garmentCount` varchar(250) NOT NULL,
  `message` varchar(250) NOT NULL,
  `status` varchar(250) NOT NULL,
  `username` varchar(250) NOT NULL,
  `mess` varchar(250) NOT NULL,
  `payment` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `bookapp`
--


-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `username` varchar(250) NOT NULL,
  `age` varchar(250) NOT NULL,
  `gender` varchar(250) NOT NULL,
  `mobile` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `regtb`
--

