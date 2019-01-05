# compare-NBA-stats


An easy to use tool that uses nba_scrape (a Python utility to scrape professional basketball data off stats.nba.com using Selenium and BeautifulSoup) to:
a) grab an NBA player's stats over a given time frame, and put it into a nicely formatted table 
OR
b) compare two players' stats over a certain season range (does not have to be the same range, e.g: Michael Jordan in 1995-97 vs Lebron James in 2006-08)

An example of a call to grab a player's stats individually would be 

`import nba

nba.player_stats(['pts', '3p%', 'stl'], '2014-18', 'stephen curry', 'season')
`

An example of a comparison would be 

`import nba

nba.compare_stats(['pts', '3p%', 'stl'], ['1985-90', '2009-14'], ['michael jordan', 'lebron james'], 'season')
`
