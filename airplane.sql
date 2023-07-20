-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2023-05-07 09:54:20
-- 服务器版本： 10.4.27-MariaDB
-- PHP 版本： 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `airplane`
--

-- --------------------------------------------------------

--
-- 表的结构 `agent`
--

CREATE TABLE `agent` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `booking_agent_id` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `agent`
--

INSERT INTO `agent` (`email`, `password`, `booking_agent_id`) VALUES
('mercury', 'Mercury', '12345');

-- --------------------------------------------------------

--
-- 表的结构 `airline`
--

CREATE TABLE `airline` (
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `airline`
--

INSERT INTO `airline` (`name`) VALUES
('AA'),
('Air France'),
('American Airlines'),
('British Airways'),
('China Eastern'),
('CP'),
('Emirates'),
('Lufthansa');

-- --------------------------------------------------------

--
-- 表的结构 `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `date_of_birth` varchar(30) DEFAULT NULL,
  `permission_id` int(11) NOT NULL,
  `name_airline` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `airline_staff`
--

INSERT INTO `airline_staff` (`username`, `password`, `first_name`, `last_name`, `date_of_birth`, `permission_id`, `name_airline`) VALUES
('12345', '12345678', 'li', 'yi', '2000-01-01', 89, 'American Airlines'),
('KevinLee', '13242435', 'YiTan', 'Li', '2003-01-02', 89, 'China Eastern'),
('lyt', '12345678', 'li', 'yi', '2000-01-01', 90, 'American Airlines'),
('TA', '12345678', 'T', 'A', '2000-01-01', 88, 'American Airlines');

-- --------------------------------------------------------

--
-- 表的结构 `airplane`
--

CREATE TABLE `airplane` (
  `id` varchar(30) NOT NULL,
  `name_airline` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `airplane`
--

INSERT INTO `airplane` (`id`, `name_airline`) VALUES
('1-110', 'China Eastern'),
('1-119', 'CP'),
('1-120', 'American Airlines'),
('1-130', 'Lufthansa'),
('1-140', 'Emirates'),
('1-150', 'Air France'),
('1-160', 'British Airways'),
('1-892', 'American Airlines'),
('3434', 'American Airlines');

-- --------------------------------------------------------

--
-- 表的结构 `airport`
--

CREATE TABLE `airport` (
  `name` varchar(50) NOT NULL,
  `city` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `airport`
--

INSERT INTO `airport` (`name`, `city`) VALUES
('CDG', 'Paris'),
('DXB', 'Dubai'),
('JFK', 'NYC'),
('LAX', 'Los Angeles'),
('LHR', 'London'),
('PVG', 'Shanghai'),
('SIN', 'Singapore'),
('TIA', 'Tokyo');

-- --------------------------------------------------------

--
-- 表的结构 `customer`
--

CREATE TABLE `customer` (
  `email` varchar(30) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `building_number` varchar(30) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `phone_number` varchar(30) DEFAULT NULL,
  `passport_number` varchar(30) DEFAULT NULL,
  `passport_expiration` varchar(30) DEFAULT NULL,
  `passport_country` varchar(30) DEFAULT NULL,
  `date_of_birth` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `customer`
--

INSERT INTO `customer` (`email`, `name`, `password`, `building_number`, `street`, `city`, `state`, `phone_number`, `passport_number`, `passport_expiration`, `passport_country`, `date_of_birth`) VALUES
('114514', '陆', '114514', '114', '514', 'Shanghai', 'Shanghai', '114', '514', '114514', 'China', '2000-01-01'),
('13621755931', '李一郯', '13242435qQ', '128', 'China Shanghai Minhang District Baochun Rd, Lane12', 'Shanghai', 'Shanghai', '+8664125534', '1', '2023-3-31', 'China', '2003-01-02');

-- --------------------------------------------------------

--
-- 表的结构 `flight`
--

CREATE TABLE `flight` (
  `flight_num` varchar(30) NOT NULL,
  `depart_time` datetime(6) DEFAULT NULL,
  `arrive_time` datetime(6) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `name_airline` varchar(30) NOT NULL,
  `plane_id` varchar(30) NOT NULL,
  `depart_airport` varchar(30) NOT NULL,
  `arrive_airport` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `flight`
--

INSERT INTO `flight` (`flight_num`, `depart_time`, `arrive_time`, `price`, `status`, `name_airline`, `plane_id`, `depart_airport`, `arrive_airport`) VALUES
('200312', '2021-01-01 00:00:00.000000', '2021-01-01 00:20:02.000000', 38000, 'in_progress', 'China Eastern', '1-110', 'JFK', 'PVG'),
('200347', '2021-01-11 00:00:00.000000', '2021-01-11 00:20:02.000000', 65000, 'in_progress', 'CP', '1-110', 'PVG', 'JFK'),
('200359', '2021-01-12 00:00:00.000000', '2021-01-12 00:20:02.000000', 12000, 'delayed', 'China Eastern', '1-119', 'JFK', 'PVG'),
('200361', '2023-01-01 00:00:00.000000', '2023-01-01 00:20:02.000000', 38000, 'in_progress', 'China Eastern', '1-110', 'JFK', 'PVG'),
('200367', '2023-01-11 00:00:00.000000', '2023-01-11 00:20:02.000000', 65000, 'in_progress', 'CP', '1-110', 'PVG', 'JFK'),
('200379', '2023-01-12 00:00:00.000000', '2023-01-12 00:20:02.000000', 12000, 'delayed', 'China Eastern', '1-119', 'JFK', 'PVG'),
('200380', '2023-01-02 07:00:00.000000', '2023-01-02 07:20:00.000000', 35000, 'in_progress', 'American Airlines', '1-120', 'LAX', 'LHR'),
('200381', '2023-01-03 12:30:00.000000', '2023-01-03 12:50:00.000000', 41000, 'delayed', 'Lufthansa', '1-130', 'LHR', 'SIN'),
('200382', '2023-01-04 18:00:00.000000', '2023-01-04 18:20:00.000000', 40000, 'cancelled', 'Emirates', '1-140', 'SIN', 'CDG'),
('200383', '2023-01-05 15:00:00.000000', '2023-01-05 15:20:00.000000', 33000, 'in_progress', 'Air France', '1-150', 'CDG', 'DXB'),
('200384', '2023-01-06 22:00:00.000000', '2023-01-06 22:20:00.000000', 37000, 'delayed', 'British Airways', '1-160', 'DXB', 'TIA'),
('200385', '2023-01-07 08:00:00.000000', '2023-01-07 08:20:00.000000', 39000, 'in_progress', 'American Airlines', '1-120', 'TIA', 'JFK'),
('200386', '2023-01-08 11:00:00.000000', '2023-01-08 11:20:00.000000', 42000, 'cancelled', 'Lufthansa', '1-130', 'JFK', 'PVG'),
('200387', '2023-01-09 14:00:00.000000', '2023-01-09 14:20:00.000000', 36000, 'in_progress', 'Emirates', '1-140', 'PVG', 'TIA'),
('200388', '2023-01-10 10:00:00.000000', '2023-01-10 10:20:00.000000', 32000, 'delayed', 'Air France', '1-150', 'TIA', 'LAX'),
('200389', '2023-01-11 21:00:00.000000', '2023-01-11 21:20:00.000000', 45000, 'in_progress', 'British Airways', '1-160', 'LAX', 'LHR'),
('200390', '2023-01-12 19:00:00.000000', '2023-01-12 19:20:00.000000', 43000, 'in_progress', 'China Eastern', '1-110', 'LHR', 'SIN'),
('200391', '2023-01-13 13:00:00.000000', '2023-01-13 13:20:00.000000', 34000, 'delayed', 'CP', '1-119', 'SIN', 'CDG'),
('200392', '2023-05-10 09:00:00.000000', '2023-05-10 09:20:00.000000', 46000, 'cancelled', 'American Airlines', '1-120', 'CDG', 'DXB'),
('200393', '2023-05-11 16:00:00.000000', '2023-05-11 16:20:00.000000', 41000, 'up_coming', 'Lufthansa', '1-130', 'DXB', 'TIA'),
('200394', '2023-05-12 20:00:00.000000', '2023-05-12 20:20:00.000000', 38000, 'up_coming', 'Emirates', '1-140', 'TIA', 'JFK'),
('200395', '2023-05-13 17:00:00.000000', '2023-05-13 17:20:00.000000', 40000, 'up_coming', 'Air France', '1-150', 'JFK', 'PVG'),
('200396', '2023-05-14 14:00:00.000000', '2023-05-14 14:20:00.000000', 39000, 'up_coming', 'British Airways', '1-160', 'PVG', 'TIA'),
('200397', '2023-05-15 21:00:00.000000', '2023-05-15 21:20:00.000000', 42000, 'up_coming', 'China Eastern', '1-110', 'TIA', 'LAX'),
('200398', '2023-05-16 18:00:00.000000', '2023-05-16 18:20:00.000000', 43000, 'up_coming', 'CP', '1-119', 'LAX', 'LHR'),
('200399', '2023-05-17 10:00:00.000000', '2023-05-17 10:20:00.000000', 35000, 'cancelled', 'American Airlines', '1-120', 'LHR', 'SIN'),
('200400', '2023-05-18 22:00:00.000000', '2023-05-18 22:20:00.000000', 36000, 'in_progress', 'Lufthansa', '1-130', 'SIN', 'CDG'),
('200401', '2023-05-19 15:00:00.000000', '2023-05-19 15:20:00.000000', 44000, 'delayed', 'Emirates', '1-140', 'CDG', 'DXB'),
('200402', '2023-05-20 10:00:00.000000', '2023-05-20 10:20:00.000000', 45000, 'in_progress', 'Lufthansa', '1-130', 'LAX', 'CDG'),
('200403', '2023-05-21 14:00:00.000000', '2023-05-21 14:20:00.000000', 46000, 'delayed', 'American Airlines', '1-120', 'CDG', 'PVG'),
('200404', '2023-05-22 08:00:00.000000', '2023-05-22 08:20:00.000000', 39000, 'cancelled', 'Emirates', '1-140', 'PVG', 'LHR'),
('200405', '2023-05-23 16:00:00.000000', '2023-05-23 16:20:00.000000', 43000, 'in_progress', 'Air France', '1-150', 'LHR', 'JFK'),
('200406', '2023-05-24 21:00:00.000000', '2023-05-24 21:20:00.000000', 36000, 'delayed', 'British Airways', '1-160', 'JFK', 'SIN'),
('200407', '2023-05-25 07:00:00.000000', '2023-05-25 07:20:00.000000', 42000, 'cancelled', 'China Eastern', '1-110', 'SIN', 'TIA'),
('200408', '2023-05-26 11:00:00.000000', '2023-05-26 11:20:00.000000', 40000, 'in_progress', 'CP', '1-119', 'TIA', 'DXB'),
('200409', '2023-05-27 19:00:00.000000', '2023-05-27 19:20:00.000000', 35000, 'delayed', 'Lufthansa', '1-130', 'DXB', 'LAX'),
('200410', '2023-05-28 22:00:00.000000', '2023-05-28 22:20:00.000000', 38000, 'cancelled', 'American Airlines', '1-120', 'LAX', 'CDG'),
('200411', '2023-05-29 13:00:00.000000', '2023-05-29 13:20:00.000000', 41000, 'in_progress', 'Emirates', '1-140', 'CDG', 'PVG'),
('200412', '2023-05-30 17:00:00.000000', '2023-05-30 17:20:00.000000', 37000, 'delayed', 'Air France', '1-150', 'PVG', 'LHR'),
('200413', '2023-05-31 09:00:00.000000', '2023-05-31 09:20:00.000000', 44000, 'cancelled', 'British Airways', '1-160', 'LHR', 'JFK');

-- --------------------------------------------------------

--
-- 表的结构 `permission`
--

CREATE TABLE `permission` (
  `permission_id` int(11) NOT NULL,
  `is_operator` int(11) NOT NULL,
  `is_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `permission`
--

INSERT INTO `permission` (`permission_id`, `is_operator`, `is_admin`) VALUES
(88, 0, 0),
(89, 1, 0),
(90, 0, 1);

-- --------------------------------------------------------

--
-- 表的结构 `ticket`
--

CREATE TABLE `ticket` (
  `ticket_id` int(11) NOT NULL,
  `flight_num` varchar(30) NOT NULL,
  `customer_email` varchar(30) NOT NULL,
  `agent_email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `ticket`
--

INSERT INTO `ticket` (`ticket_id`, `flight_num`, `customer_email`, `agent_email`) VALUES
(18, '200361', '13621755931', NULL),
(22, '200361', '13621755931', 'mercury'),
(24, '200361', '13621755931', 'mercury'),
(25, '200397', '13621755931', 'mercury'),
(26, '200361', '13621755931', 'mercury'),
(27, '200361', '13621755931', 'mercury'),
(28, '200361', '13621755931', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `works_for`
--

CREATE TABLE `works_for` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 转存表中的数据 `works_for`
--

INSERT INTO `works_for` (`name`, `email`) VALUES
('China Eastern', 'mercury');

--
-- 转储表的索引
--

--
-- 表的索引 `agent`
--
ALTER TABLE `agent`
  ADD PRIMARY KEY (`email`);

--
-- 表的索引 `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`name`);

--
-- 表的索引 `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `permission_id` (`permission_id`),
  ADD KEY `name_airline` (`name_airline`);

--
-- 表的索引 `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`id`,`name_airline`),
  ADD KEY `name_airline` (`name_airline`);

--
-- 表的索引 `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`name`);

--
-- 表的索引 `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email`);

--
-- 表的索引 `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`flight_num`,`name_airline`),
  ADD KEY `name_airline` (`name_airline`),
  ADD KEY `plane_id` (`plane_id`),
  ADD KEY `depart_airport` (`depart_airport`),
  ADD KEY `arrive_airport` (`arrive_airport`);

--
-- 表的索引 `permission`
--
ALTER TABLE `permission`
  ADD PRIMARY KEY (`permission_id`,`is_operator`,`is_admin`);

--
-- 表的索引 `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ticket_id`),
  ADD KEY `flight_num` (`flight_num`),
  ADD KEY `customer_email` (`customer_email`),
  ADD KEY `agent_email` (`agent_email`);

--
-- 表的索引 `works_for`
--
ALTER TABLE `works_for`
  ADD PRIMARY KEY (`name`,`email`),
  ADD KEY `email` (`email`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `ticket`
--
ALTER TABLE `ticket`
  MODIFY `ticket_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- 限制导出的表
--

--
-- 限制表 `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`permission_id`),
  ADD CONSTRAINT `airline_staff_ibfk_2` FOREIGN KEY (`name_airline`) REFERENCES `airline` (`name`);

--
-- 限制表 `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`name_airline`) REFERENCES `airline` (`name`);

--
-- 限制表 `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`name_airline`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`plane_id`) REFERENCES `airplane` (`id`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`depart_airport`) REFERENCES `airport` (`name`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`arrive_airport`) REFERENCES `airport` (`name`);

--
-- 限制表 `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`flight_num`) REFERENCES `flight` (`flight_num`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`),
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`agent_email`) REFERENCES `agent` (`email`);

--
-- 限制表 `works_for`
--
ALTER TABLE `works_for`
  ADD CONSTRAINT `works_for_ibfk_1` FOREIGN KEY (`name`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `works_for_ibfk_2` FOREIGN KEY (`email`) REFERENCES `agent` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
