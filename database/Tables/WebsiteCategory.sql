DROP TABLE IF EXISTS WebsiteCategory;

CREATE TABLE WebsiteCategory (
	ID int auto_increment not NULL primary key,
	Website_ID int not NULL,
  Category_ID int not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE WebsiteCategory AUTO_INCREMENT = 0;

INSERT WebsiteCategory (Website_ID, Category_ID) values (1,1);
INSERT WebsiteCategory (Website_ID, Category_ID) values (1,2);
INSERT WebsiteCategory (Website_ID, Category_ID) values (1,6);