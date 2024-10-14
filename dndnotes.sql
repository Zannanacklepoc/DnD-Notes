-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DnDnotes
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `DnDnotes` ;

-- -----------------------------------------------------
-- Schema DnDnotes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DnDnotes` DEFAULT CHARACTER SET utf8 ;
USE `DnDnotes` ;

-- -----------------------------------------------------
-- Table `DnDnotes`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(80) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnDnotes`.`Campaign`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`Campaign` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `time_and_date` VARCHAR(50) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Campaign_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Campaign_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `DnDnotes`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnDnotes`.`Notes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`Notes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `notes` LONGTEXT NULL,
  `date_time` DATETIME NULL,
  `Campaign_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Notes_Campaign1_idx` (`Campaign_id` ASC) VISIBLE,
  CONSTRAINT `fk_Notes_Campaign1`
    FOREIGN KEY (`Campaign_id`)
    REFERENCES `DnDnotes`.`Campaign` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnDnotes`.`NPC`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`NPC` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NULL,
  `Race` VARCHAR(45) NULL,
  `Class` VARCHAR(45) NULL,
  `location` VARCHAR(150) NULL,
  `small_discription` MEDIUMTEXT NULL,
  `NPCcol` VARCHAR(45) NULL,
  `Campaign_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_NPC_Campaign1_idx` (`Campaign_id` ASC) VISIBLE,
  CONSTRAINT `fk_NPC_Campaign1`
    FOREIGN KEY (`Campaign_id`)
    REFERENCES `DnDnotes`.`Campaign` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnDnotes`.`Quest`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`Quest` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Giver` VARCHAR(45) NOT NULL,
  `Objective` MEDIUMTEXT NULL,
  `Reward` VARCHAR(100) NULL,
  `Campaign_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Giver`),
  INDEX `fk_Quest_Campaign1_idx` (`Campaign_id` ASC) VISIBLE,
  CONSTRAINT `fk_Quest_Campaign1`
    FOREIGN KEY (`Campaign_id`)
    REFERENCES `DnDnotes`.`Campaign` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnDnotes`.`Party_Treasure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnDnotes`.`Party_Treasure` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NULL,
  `description` LONGTEXT NULL,
  `Campaign_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Party_Treasure_Campaign1_idx` (`Campaign_id` ASC) VISIBLE,
  CONSTRAINT `fk_Party_Treasure_Campaign1`
    FOREIGN KEY (`Campaign_id`)
    REFERENCES `DnDnotes`.`Campaign` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
