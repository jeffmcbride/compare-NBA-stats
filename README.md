# compare-NBA-stats


An easy to use tool that uses nba_scrape (a Python utility to scrape professional basketball data off stats.nba.com using Selenium and BeautifulSoup) to:
a) grab an NBA player's stats over a given time frame, and put it into a nicely formatted table 
OR
b) compare two players' stats over a certain season range (does not have to be the same range, e.g: Michael Jordan in 1995-97 vs Lebron James in 2006-08)

An example of a call to grab a player's stats individually would be 

`import nba
nba.player_stats(['pts', '3p%', 'stl'], '2014-18', 'stephen curry', 'season')
`
Which would give you a table that looks like the following:

stephen curry yrs     pts    3p%    stl
-------------------  -----  -----  -----
2014-15               23.8   44.3    2
2015-16               30.1   45.4    2.1
2016-17               25.3   41.1    1.8
2017-18               26.4   42.3    1.6

An example of a comparison would be 

`import nba
nba.compare_stats(['pts', '3p%', 'stl'], ['1985-90', '2009-14'], ['michael jordan', 'lebron james'], 'season')
`
Which would give you a table that looks like the following:

michael jordan yrs    lebron james yrs      michael jordan pts    lebron james pts    michael jordan 3p%    lebron james 3p%    michael jordan stl    lebron james stl
--------------------  ------------------  --------------------  ------------------  --------------------  ------------------  --------------------  ------------------
1985-86               2009-10                             22.7                29.7                  16.7                33.3                   2.1                 1.6
1986-87               2010-11                             37.1                26.7                  18.2                33                     2.9                 1.6
1987-88               2011-12                             35                  27.1                  13.2                36.2                   3.2                 1.9
1988-89               2012-13                             32.5                26.8                  27.6                40.6                   2.9                 1.7
1989-90               2013-14                             33.6                27.1                  37.6                37.9                   2.8                 1.6
