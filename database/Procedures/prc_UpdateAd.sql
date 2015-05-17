DROP PROCEDURE IF EXISTS prc_UpdateAd;

CREATE PROCEDURE AdMania.`prc_UpdateAd`(
	paramAdID INT, 
	paramAdvertiserID INT, 
  paramAdvertiserName varchar(50),
  paramCategory varchar(50),
	paramStartDate varchar(50), 
	paramEndDate varchar(50),
  paramHeight int,
  paramWidth int,
	paramHTML varchar(2000))
BEGIN
	IF paramStartDate = 'None' THEN SET paramStartDate = NULL; END IF;
	IF paramEndDate = 'None' THEN SET paramEndDate = NULL; END IF;

	IF EXISTS (SELECT 1	FROM Ad WHERE AdID = paramAdID AND AdvertiserID = paramAdvertiserID LIMIT 1) THEN
		UPDATE Ad
		SET AdvertiserName = paramAdvertiserName,
        Category = paramCategory,
        Height = paramHeight,
        Width = paramWidth,
        StartDate = coalesce(paramStartDate, '1900-01-01'),
			  EndDate = coalesce(paramEndDate, '2999-12-31'),
			  HTML = paramHTML
		WHERE AdID = paramAdID AND AdvertiserID = paramAdvertiserID;
	ELSE
		INSERT Ad (
			AdID, 
			AdvertiserID, 
      AdvertiserName,
      Category,
			StartDate, 
			EndDate, 
      Height,
      Width,
			HTML)
		VALUES (
			paramAdID, 
			paramAdvertiserID, 
      paramAdvertiserName,
      paramCategory,
			coalesce(paramStartDate, '1900-01-01'), 
			coalesce(paramEndDate, '2999-12-31'),
      paramHeight,
      paramWidth,
			paramHTML);
	END IF;
END;

GRANT EXECUTE ON PROCEDURE AdMania.prc_UpdateAd to 'adservicer'@'%';;
