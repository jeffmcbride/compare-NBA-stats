from nba_scrape import NBA
from tabulate import tabulate

def player_stats(stats, years, p1, mode):

    league = NBA()
    player = league.get_player(p1)
    yrs = []
    p = player.get_stats(stats, years, mode)
    results = []
    for years in p:
        yrs.append(years)

    for i in range(len(yrs)):
        tuple = (yrs[i],)
        for j in range(len(stats)):
            tuple = tuple + (p[yrs[i]][j],)
        results.append(tuple)
        
    
    colNames = [p1 + " yrs"]
    for sts in stats:
        colNames.append(sts)
       

    print(tabulate(results, headers=colNames))
        
        
        
def compare_stats(stats, years, players, mode):
    '''
    Example of a call:
    compare_stats(['pts', 'stl'], ['2017-18'], ['stephen curry', 'lebron james'], 'season')
    '''
    
    league = NBA()
    player1 = league.get_player(players[0])
    player2 = league.get_player(players[1])
    p1yrs = []
    p2yrs = []
    results = []
    p1 = player1.get_stats(stats, years[0], mode)
    p2 = player2.get_stats(stats, years[-1], mode)
    for years in p1:
        p1yrs.append(years)
        
    for years in p2:
        p2yrs.append(years)
      
    
    if (len(p1yrs) != len(p2yrs)):
        print("Need to compare the same amount of seasons")
        return
    
    for i in range(len(p1yrs)):
        tuple = (p1yrs[i], p2yrs[i])
        for j in range(len(stats)):
            tuple = tuple + (p1[p1yrs[i]][j], p2[p2yrs[i]][j])
        results.append(tuple)
    
    
    colNames = [players[0] + ' yrs', players[1] + ' yrs']
    for sts in stats:
        colNames.append(players[0] + " " + sts)
        colNames.append(players[1] + " " + sts)

    print(tabulate(results, headers=colNames))
    