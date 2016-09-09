USE mydb;
CREATE TABLE `mydb`.`emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email_address` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`));


ALTER TABLE `mydb`.`emails` 
CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT ,
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL ;