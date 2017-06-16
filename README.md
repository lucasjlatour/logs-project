# logs-project
## Core Features
Run this program to show you the top viewed pages, most popular authors, and days with errors over 1%. It runs querys on the news database to get these results.



## Usage
To use this program run log.py with python3. Make sure to prepare the software and data according to instructions in Logs Project Section 3. After preparing software and data, save log.py in /vagrant. 

The news database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

Before using, you need to create a view in the database for the program to run properly.

CREATE VIEW auth_views AS SELECT articles.author, COUNT(log.path) AS views FROM articles, log, authors WHERE '/article/' || articles.slug = log.path AND log.status = '200 OK' GROUP BY articles.author;


## Expected Output
Refer to output.txt in this project folder

## Authorship

All code was written by Lucas La Tour as part of the Udacity Full Stack Nanodegree.

## License 
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>



