# logsAnalysis
logsAnalysis is a reporting tool that generates reports based on the news database. Specifically, it prints
the most popular authors and articles in the database, as well as the days in which the request error
percentage exceeded 1%. 


# Installation
Clone the GitHub repository.

# Create view commands
Add the following views to the news database:

    create view articles_simplified as
       select name, title, path 
       from log, articles, authors
       where (path like '%'||slug||'%') and (authors.id=articles.author);

    create view day_error as
        select date_trunc('day',time) as day1, count(*) as "num_errors"
        from log 
        where status='404 NOT FOUND' 
        group by day1;

    create view day_requests as
        select date_trunc('day',time) as day2, count(*) as "num_accessed"
        from log 
        group by day2;
        
# Usage
After creating the views in the news database, open newsdata.py in IDLE and run the script to generate the report.
       
       
