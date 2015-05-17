DROP TABLE IF EXISTS WebsiteAd;

CREATE TABLE WebsiteAd (
	ID int auto_increment not NULL primary key,
	Website_ID int not NULL,
  Ad_ID int not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE WebsiteAd AUTO_INCREMENT = 0;

INSERT WebsiteAd (Website_ID, Ad_ID) 
SELECT 1, ad.ID FROM Ad ad
JOIN Advertiser av ON ad.AdvertiserID = av.AdvertiserID
JOIN Category c ON ad.Category = c.Category and c.Affiliate_ID = av.Affiliate_ID
JOIN WebsiteCategory wc on c.ID = wc.Category_ID
WHERE ad.Height = ad.Width and ad.Height BETWEEN 150 AND 250
LIMIT 9;
