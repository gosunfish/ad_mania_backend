DROP TABLE IF EXISTS Website;

CREATE TABLE Website (
	ID int auto_increment not NULL primary key,
	Website varchar(50) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE Website AUTO_INCREMENT = 0;

INSERT Website (Website) values ('earthtravelers.com');
INSERT Website (Website) values ('coupongear.com');