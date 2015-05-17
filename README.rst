Ad Mania


Background:
EarthTravelers.com is a website that renders advertisements for a variety of travel companies. The advertisements are obtained from CJ.com, an affiliate platform. Advertisers post advertisements in the form of HTML code snippets on CJ.com. The advertisements are hand selected, cut and pasted onto EarthTravelers.com. 

Problem:
The manual approach has limited scalability. The plan is to add a few websites in the near future, and grow the number indefinitely over time.

Solution:
Use the CJ.com APIs to develop an automated system that will select advertisements based on categories, dates and banner size. Render dynamic websites using these advertisements.

The solution should include logging for analyzing performance by advertisement, web page, position of advertisement on the page, etc.

Wish List:
Introduce new, more interesting templates to the dynamic selection and rendering system.
Support AB testing of templates, AB testing of advertisement positioning, etc.
Take performance into consideration in the automated advertisement selection process.

Technical notes:
To start mysql locally, run this:
sudo /Library/StartupItems/MySQLCOM/MySQLCOM start

To connect to AWS mysql database:
mysql -h dizzyninjal.ctbrqcon0iyi.us-east-1.rds.amazonaws.com -P 3306 -u sa -p r.......
mysql -h web-sites.cqnknvzsrvqd.us-east-1.rds.amazonaws.com -P 3306 -u admin -p S1......

BUILD NOTES:
sudo chown carolyn.evans: /var/log/admania.log



