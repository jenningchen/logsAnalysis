# logsAnalysis
logsAnalysis is a reporting tool that generates reports based on the news database. Specifically, it prints
the most popular authors and articles in the database, as well as the days in which the request error
percentage exceeded 1%. 

# Installation
Clone the GitHub repository. Add the file newsdata.sql. [Click here to download]( https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Then use the command `psql -d news -f newsdata.sql` to load the data.

# The news database
The news database was included as part of the Udacity VM configuration and forms the backend of a newspaper site. The database contains newspaper articles and a web server log. 

# Create view commands
Add the following views to the news database:

```sql
    CREATE VIEW articles_simplified AS
       SELECT name, title, path 
       FROM log, articles, authors
       WHERE (path LIKE '%'||slug) AND (authors.id=articles.author);

    CREATE VIEW day_error AS
        SELECT date_trunc('day',time) AS day1, count(*) AS "num_errors"
        FROM log 
        WHERE status='404 NOT FOUND' 
        GROUP BY day1;

    CREATE VIEW day_requests AS
        SELECT date_trunc('day',time) AS day2, count(*) AS "num_accessed"
        FROM log 
        GROUP BY day2;
```
        
# Usage
After creating the views in the news database, open newsdata.py in IDLE and run the script to generate the report.
       
       
