DROP USER 'adservicer'@'%';
CREATE USER 'adservicer'@'%' IDENTIFIED BY 'a020d4@71F0f';
GRANT SELECT ON Ad TO 'adservicer'@'%';
GRANT INSERT ON Ad TO 'adservicer'@'%';

DROP USER 'adservice'@'%';
CREATE USER 'adservice'@'%' IDENTIFIED BY 'f72!7E20f100';
GRANT SELECT ON Ad TO 'adservice'@'%';



