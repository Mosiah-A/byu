-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema store
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `store` ;

-- -----------------------------------------------------
-- Schema store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `store` DEFAULT CHARACTER SET utf8 ;
USE `store` ;

-- -----------------------------------------------------
-- Table `store`.`costumer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `store`.`costumer` ;

CREATE TABLE IF NOT EXISTS `store`.`costumer` (
  `costumer_id` INT NOT NULL,
  `fisrt_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`costumer_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store`.`order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `store`.`order` ;

CREATE TABLE IF NOT EXISTS `store`.`order` (
  `order_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `costumer_costumer_id` INT NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `fk_order_costumer_idx` (`costumer_costumer_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_costumer`
    FOREIGN KEY (`costumer_costumer_id`)
    REFERENCES `store`.`costumer` (`costumer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store`.`product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `store`.`product` ;

CREATE TABLE IF NOT EXISTS `store`.`product` (
  `product_id` INT NOT NULL,
  `prod_name` VARCHAR(45) NOT NULL,
  `prod_price` DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store`.`order_detail`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `store`.`order_detail` ;

CREATE TABLE IF NOT EXISTS `store`.`order_detail` (
  `order_order_id` INT NOT NULL,
  `product_product_id` INT NOT NULL,
  `order_detailcol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`order_order_id`, `product_product_id`),
  INDEX `fk_order_has_product_product1_idx` (`product_product_id` ASC) VISIBLE,
  INDEX `fk_order_has_product_order1_idx` (`order_order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_product_order1`
    FOREIGN KEY (`order_order_id`)
    REFERENCES `store`.`order` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_product_product1`
    FOREIGN KEY (`product_product_id`)
    REFERENCES `store`.`product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
