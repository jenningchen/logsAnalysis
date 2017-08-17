#!/usr/bin/env python3

# Reporting tool that generates reports based on data provided

import psycopg2
import datetime
import calendar


def main():
    '''Print most popular 3 articles of all time.'''
    get_articles()
    '''Print most popular authors of all time.'''
    get_authors()
    '''Days where more than 1% of requests led to errors.'''
    get_errors()


def get_articles():
    print("Ranking of most popular 3 articles of all time:")
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query1 = """select title, count(*) as views
        from articles_simplified
        group by title
        order by views desc limit 3;"""
    c.execute(query1)
    rows = c.fetchall()

    '''Print result'''
    for row in rows:
        print("%s — %s views" % (row[0], row[1]))
    db.close()
    print ("\n")


def get_authors():
    print("Ranking of most popular authors of all time:")
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query2 = """select name, count(*) as views
        from articles_simplified
        group by name
        order by views desc;"""
    c.execute(query2)
    rows = c.fetchall()

    '''Print result'''
    for row in rows:
        print("%s — %s views" % (row[0], row[1]))
    db.close()
    print("\n")


def get_errors():
    print("Day(s) where more than 1% of requests led to errors:")
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query3 = """select day1, num_errors, num_accessed
        from day_error join day_requests on day1=day2
        where ((num_errors::float/num_accessed) > 0.01);"""
    c.execute(query3)
    rows = c.fetchall()

    '''Print result'''
    for row in rows:
        index = row[0].month
        print("%s %s, %s — %.2f%% errors"
              % (calendar.month_name[index], row[0].day, row[0].year,
                 (100*row[1]/row[2])))
    db.close()
    print("\n")


main()
