

CREATE TABLE `address` (
  `AddressID` int NOT NULL AUTO_INCREMENT,
  `Street` varchar(25) DEFAULT NULL,
  `City` varchar(25) DEFAULT NULL,
  `State` varchar(25) DEFAULT NULL,
  `Zipcode` decimal(9,0) DEFAULT NULL,
  PRIMARY KEY (`AddressID`),
  UNIQUE KEY `AddressID_UNIQUE` (`AddressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `officer` (
  `OfficerID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  `AddressID` int DEFAULT NULL,
  `RespDesc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`OfficerID`),
  UNIQUE KEY `OfficerID_UNIQUE` (`OfficerID`),
  KEY `FK_Officer_AddressID_idx` (`AddressID`),
  CONSTRAINT `FK_Officer_AddressID` FOREIGN KEY (`AddressID`) REFERENCES `address` (`AddressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `jobtitle` (
  `JobTitleID` int NOT NULL AUTO_INCREMENT,
  `JobTitle` varchar(45) NOT NULL,
  `OfficerID` int NOT NULL,
  `Salary` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`JobTitleID`),
  UNIQUE KEY `JobTitleID_UNIQUE` (`JobTitleID`),
  KEY `FK_JobTitle_OfficerID_idx` (`OfficerID`),
  CONSTRAINT `FK_JobTitle_OfficerID` FOREIGN KEY (`OfficerID`) REFERENCES `officer` (`officerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `office` (
  `officeid` int NOT NULL AUTO_INCREMENT,
  `OfficeName` varchar(45) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `officerid` int DEFAULT NULL,
  PRIMARY KEY (`officeid`),
  UNIQUE KEY `officeid_UNIQUE` (`officeid`),
  UNIQUE KEY `OfficeName_UNIQUE` (`OfficeName`),
  KEY `FK_officerid_idx` (`officerid`),
  CONSTRAINT `FK_Office_OfficerID` FOREIGN KEY (`officerid`) REFERENCES `officer` (`OfficerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `event` (
  `EventCode` int NOT NULL AUTO_INCREMENT,
  `EventName` varchar(45) NOT NULL,
  `OfficerID` int DEFAULT NULL,
  `MissionDesc` varchar(225) DEFAULT NULL,
  `DateOfVolunteer` date DEFAULT NULL,
  `AttendingNeed` decimal(8,0) DEFAULT NULL,
  `AddressID` int DEFAULT NULL,
  `PhoneNumber` int DEFAULT NULL,
  `NumberAttended` decimal(8,0) DEFAULT NULL,
  `ObjectiveDesc` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`EventCode`),
  UNIQUE KEY `EventID_UNIQUE` (`EventCode`),
  KEY `FK_Event_Officer_idx` (`OfficerID`),
  KEY `FK_Event_AddressID_idx` (`AddressID`),
  CONSTRAINT `FK_Event_AddressID` FOREIGN KEY (`AddressID`) REFERENCES `address` (`AddressID`),
  CONSTRAINT `FK_Event_Officer` FOREIGN KEY (`OfficerID`) REFERENCES `officer` (`OfficerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `volunteer` (
  `VolunteerID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  `AddressID` int DEFAULT NULL,
  `RespDesc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`VolunteerID`),
  UNIQUE KEY `VolunteerID_UNIQUE` (`VolunteerID`),
  KEY `FK_Volunteer_AddressID_idx` (`AddressID`),
  CONSTRAINT `FK_Volunteer_AddressID` FOREIGN KEY (`AddressID`) REFERENCES `address` (`AddressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `volunteerevent` (
  `VolunteerEventID` int NOT NULL AUTO_INCREMENT,
  `VolunteerID` int DEFAULT NULL,
  `EventCode` int DEFAULT NULL,
  `RequestDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `SignUpDate` date DEFAULT NULL,
  PRIMARY KEY (`VolunteerEventID`),
  UNIQUE KEY `VolunteerEventID_UNIQUE` (`VolunteerEventID`),
  KEY `FK_VolunteerEvent_VolunteerID_idx` (`VolunteerID`),
  KEY `FK_VolunteerEvent_EventCode_idx` (`EventCode`),
  CONSTRAINT `FK_VolunteerEvent_EventCode` FOREIGN KEY (`EventCode`) REFERENCES `event` (`EventCode`),
  CONSTRAINT `FK_VolunteerEvent_VolunteerID` FOREIGN KEY (`VolunteerID`) REFERENCES `volunteer` (`VolunteerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;





