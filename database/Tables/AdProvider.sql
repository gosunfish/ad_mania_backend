DROP TABLE IF EXISTS AdProvider;

CREATE TABLE AdProvider (
	ID int auto_increment not NULL primary key,
	AdProviderName varchar(50) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE AdProvider AUTO_INCREMENT = 0;

INSERT AdProvider (AdProviderName) values ('CJ');
INSERT AdProvider (AdProviderName) values ('ShareASale');