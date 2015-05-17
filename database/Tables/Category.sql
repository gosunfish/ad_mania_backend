DROP TABLE IF EXISTS Category;

CREATE TABLE Category (
	ID int auto_increment not NULL primary key,
  AdProvider_ID int not NULL,
	Category varchar(50) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE Category AUTO_INCREMENT = 0;

INSERT Category (AdProvider_ID, Category) 
SELECT DISTINCT 1, Category from Ad;
