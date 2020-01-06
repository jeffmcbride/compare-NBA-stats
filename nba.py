import matplotlib.pyplot as plt
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.static import teams



'''Available team stats:
    TEAM_ID, TEAM_CITY, TEAM_NAME, YEAR, GP, WINS, LOSSES, WIN_PCT, CONF_RANK, 
    DIV_RANK, PO_WINS, PO_LOSSES, CONF_COUNT, DIV_COUNT, NBA_FINALS_APPEARANCE, 
    FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, 
    AST, PF, STL, TOV, BLK, PTS, PTS_RANK'''
    
class Team:
    
    def __init__(self, name, start, end):
        self.search_name = name
        self.start = start
        self.end = end
        self.duration = end - start
        self.teamid = teams.find_teams_by_full_name(self.search_name)[0]['id']
        self.teamstats = teamyearbyyearstats.TeamYearByYearStats(self.teamid).get_data_frames()
        self.teamname = self.teamstats[0]['TEAM_NAME'].iloc[-1]
        
        
    def get_stats(self, stat):
        return self.teamstats[0].set_index("YEAR")[stat]
        
        
    def graph_stats(self, stat):
        stats = self.get_stats(stat)
        ax = stats.plot()
        ax.legend([self.teamname + ' ' + stat]);
        
        
        
def graphTwoTeams(Team1, Team2, stat):
    # Create dataframe of years and stat
    pass


        
raps = Team('rap', 5, 4)
raps.graph_stats('WINS')






