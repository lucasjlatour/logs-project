#!/usr/bin/env python
import psycopg2
db = psycopg2.connect(database="news")
c = db.cursor()


def get_top_articles():
    '''Get the top viewed pages from DB'''
    c.execute('''SELECT articles.title, COUNT(log.path) AS views
                 FROM log, articles
                 WHERE '/article/' || articles.slug = log.path
                 GROUP BY articles.title ORDER BY views DESC LIMIT 3;''')
    articles = c.fetchall()
    print("\nTop viewed articles:")
    n = 0
    while n < len(articles):
        print(str(articles[n][0]) + " -- " + str(articles[n][1]) + " views")
        n = n + 1


def get_top_authors():
    '''List the most popular authors'''
    c.execute('''SELECT authors.name, auth_views.views
                 FROM authors, auth_views
                 WHERE authors.id = auth_views.author
                 ORDER BY auth_views.views DESC;''')
    authors = c.fetchall()
    print("\nTop viewed authors:")
    n = 0
    while n < len(authors):
        print(str(authors[n][0]) + " -- " + str(authors[n][1]) + " views")
        n = n + 1


def get_log_errors():
    '''Gets all days with 404 Errors greater than one percent.'''
    c.execute('''SELECT tot_errors.date, tot_errors.count, dayviews.count,
                 tot_errors.count*1.0/dayviews.count as error_rate
                 FROM (SELECT DATE(time), COUNT(*)
                       FROM log GROUP BY DATE(time)) as dayviews,
                      (SELECT errors.date, COUNT(*)
                       FROM (SELECT DATE(time), status
                             FROM log WHERE status = '404 NOT FOUND') as errors
                             GROUP BY errors.date) as tot_errors
                 WHERE tot_errors.date = dayviews.date
                 AND tot_errors.count*1.0/dayviews.count > 0.01;''')
    days = c.fetchall()
    print("\nDays with errors over 1"+"%:")
    n = 0
    while n < len(days):
        err = days[n][3]*100
        err = round(err, 2)
        print(str(days[n][0]) + " -- " + str(err) + "%" + " error rate")
        n = n + 1
get_top_articles()
get_top_authors()
get_log_errors()
db.close()
