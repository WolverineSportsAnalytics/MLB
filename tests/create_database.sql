-- MySQL Script generated by MySQL Workbench
-- Sun Jun 10 18:18:30 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mlb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wnb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mlb` DEFAULT CHARACTER SET utf8 ;
USE `mlb` ;

-- -----------------------------------------------------
-- Table `mlb_test`.`box_score_urls`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mlb`.`lineups` (
  `lineupID` INT(11) NOT NULL AUTO_INCREMENT,
  `lineupNumber` INT(11) not Null,
  `date` Date,
  `P` VARCHAR(45),
  `C/1B` VARCHAR(45),
  `2B` VARCHAR(45),
  `3B` VARCHAR(45),
  `SS` VARCHAR(45),
  `OF1` VARCHAR(45),
  `OF2` VARCHAR(45),
  `OF3` VARCHAR(45),
  `UTIL` VARCHAR(45),
  `lineupTime` TIME,
  `projectedPoints` float,
  PRIMARY KEY (`lineupID`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

CREATE TABLE IF NOT EXISTS `mlb`.`players` (
  `playerTableID` INT(11) NOT NULL AUTO_INCREMENT,
  `date` Date,
  `Name` VARCHAR(45), 
  `Position` VARCHAR(45),
  `Team` VARCHAR(45),
  `Salary` float default NULL,
  `RotoWirePrediction` float default NULL,
  `RotoGrinderPrediction` float default NULL,
  PRIMARY KEY (`playerTableID`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;
