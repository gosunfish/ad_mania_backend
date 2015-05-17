DROP TABLE IF EXISTS Advertiser;

CREATE TABLE Advertiser (
	ID int auto_increment not NULL primary key,
  AdProvider_ID int not NULL,
  AdvertiserID int not NULL,
	AdvertiserName varchar(50) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE Advertiser AUTO_INCREMENT = 0;

INSERT Advertiser (AdProvider_ID, AdvertiserID, AdvertiserName) 
SELECT DISTINCT 1, AdvertiserID, AdvertiserName from Ad;
