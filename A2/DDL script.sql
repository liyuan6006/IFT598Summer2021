CREATE TABLE `officer` (
  `OfficerID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `ResponsibilityDesc` varchar(45) DEFAULT NULL,
  `JobTitleID` int DEFAULT NULL,
  PRIMARY KEY (`OfficerID`),
  UNIQUE KEY `OfficerID_UNIQUE` (`OfficerID`),
  KEY `JobTitleID_idx` (`JobTitleID`),
  CONSTRAINT `FK_Officer_JobTitleID` FOREIGN KEY (`JobTitleID`) REFERENCES `jobtitle` (`JoTitleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `office` (
  `officeid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `startdate` datetime DEFAULT NULL,
  `enddate` datetime DEFAULT NULL,
  `officerid` int DEFAULT NULL,
  PRIMARY KEY (`officeid`),
  UNIQUE KEY `officeid_UNIQUE` (`officeid`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `FK_officerid_idx` (`officerid`),
  CONSTRAINT `FK_Office_OfficerID` FOREIGN KEY (`officerid`) REFERENCES `officer` (`OfficerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `jobtitle` (
  `JoTitleID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`JoTitleID`),
  UNIQUE KEY `JoTitleID_UNIQUE` (`JoTitleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `volunteer` (
  `VolunteerID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Age` int NOT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `ResponsibilityDesc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`VolunteerID`),
  UNIQUE KEY `VolunteerID_UNIQUE` (`VolunteerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `event` (
  `EventID` int NOT NULL AUTO_INCREMENT,
  `EventName` varchar(45) NOT NULL,
  `OfficerID` int DEFAULT NULL,
  `Description` varchar(45) DEFAULT NULL,
  `DateOfVolunteer` datetime DEFAULT NULL,
  `AttendingNeed` int DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `PhoneNumber` int DEFAULT NULL,
  PRIMARY KEY (`EventID`),
  UNIQUE KEY `EventID_UNIQUE` (`EventID`),
  KEY `FK_Event_Officer_idx` (`OfficerID`),
  CONSTRAINT `FK_Event_Officer` FOREIGN KEY (`OfficerID`) REFERENCES `officer` (`OfficerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `volunteerevent` (
  `VolunteerEventID` int NOT NULL AUTO_INCREMENT,
  `VolunteerID` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  PRIMARY KEY (`VolunteerEventID`),
  UNIQUE KEY `VolunteerEventID_UNIQUE` (`VolunteerEventID`),
  KEY `FK_VolunteerEvent_VolunteerID_idx` (`VolunteerID`),
  KEY `FK_VolunteerEvent_EventID_idx` (`EventID`),
  CONSTRAINT `FK_VolunteerEvent_EventID` FOREIGN KEY (`EventID`) REFERENCES `event` (`EventID`),
  CONSTRAINT `FK_VolunteerEvent_VolunteerID` FOREIGN KEY (`VolunteerID`) REFERENCES `volunteer` (`VolunteerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci