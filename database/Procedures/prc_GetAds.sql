DROP PROCEDURE IF EXISTS prc_GetAds;

CREATE PROCEDURE AdMania.`prc_GetAds`(
	paramWebsite varchar(50))
BEGIN
  SELECT ad.HTML
  FROM Ad ad
  JOIN WebsiteAd wa ON ad.ID = wa.Ad_ID
  JOIN Website w ON wa.Website_ID = w.ID
  WHERE w.Website = paramWebsite;
END;

GRANT EXECUTE ON PROCEDURE AdMania.prc_GetAds to 'adservicer'@'%';;

call prc_GetAds('earthtravelers.com')
