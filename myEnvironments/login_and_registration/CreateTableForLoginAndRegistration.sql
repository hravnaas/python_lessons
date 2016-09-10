USE mydb;
CREATE TABLE `mydb`.`registered_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email_address` VARCHAR(255) NOT NULL,
  `pw_hash` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`));

-- ALTER TABLE `mydb`.`emails` 
-- CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT ,
-- CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL ,
-- CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL ;