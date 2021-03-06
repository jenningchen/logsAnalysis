#!/usr/bin/env python3

# Reporting tool that generates reports based on data provided

import psycopg2
import datetime
import calendar


def main():
    """Print most popular 3 articles of all time."""
    get_articles()
    """Print most popular authors of all time."""
    get_authors()
    """Days where more than 1% of requests led to errors."""
    get_errors()


def execute_query(query):
    """Executes query and returns tuple list"""
    try:
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_articles():
    """Print ranking of most popular 3 articles of all time"""

    print("Ranking of most popular 3 articles of all time:")
    query1 = """select title, count(*) as views
        from articles_simplified
        group by title
        order by views desc limit 3;"""

    rows = execute_query(query1)

    """Print result"""
    for title, views in rows:
        print('\"{}\" — {} views'.format(title, views))
    print ("\n")


def get_authors():
    """"Print ranking of most popular authors of all time"""

    print("Ranking of most popular authors of all time:")
    query2 = """select name, count(*) as views
        from articles_simplified
        group by name
        order by views desc;"""

    rows = execute_query(query2)

    '''Print result'''
    for name, views in rows:
        print('\"{}\" — {} views'.format(name, views))
    print("\n")


def get_errors():
    """"Print days where more than 1% of requests led to errors"""

    print("Day(s) where more than 1% of requests led to errors:")
    query3 = """select day1, num_errors, num_accessed
        from day_error join day_requests on day1=day2
        where ((num_errors::float/num_accessed) > 0.01);"""
    rows = execute_query(query3)

    """Print result"""
    for day1, errors, accessed in rows:
        index = day1.month
        print('{} {}, {} — {:.2f}% errors'.format(calendar.month_name[index],
              day1.day, day1.year, (100*errors/accessed)))
    print("\n")

if __name__ == '__main__':
    main()
