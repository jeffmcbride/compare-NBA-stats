import plotly
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import *


teams.find_teams_by_full_name("ca")

'''Available team stats:
    TEAM_ID, TEAM_CITY, TEAM_NAME, YEAR, GP, WINS, LOSSES, WIN_PCT, CONF_RANK,
    DIV_RANK, PO_WINS, PO_LOSSES, CONF_COUNT, DIV_COUNT, NBA_FINALS_APPEARANCE,
    FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB,
    AST, PF, STL, TOV, BLK, PTS, PTS_RANK'''

class Team:

    def __init__(self, name):
        self.search_name = name
        self.team = teams.find_teams_by_full_name(self.search_name)[0]
        self.teamid = self.team['id']
        self.teamname = self.team['nickname']
        self.teamstats = teamyearbyyearstats.TeamYearByYearStats(self.teamid).get_data_frames()[0]

    def get_stats(self, stat, start, end):
        stats_in_range = self.teamstats[self.teamstats['YEAR'] <= end]
        stats_in_range = stats_in_range[self.teamstats['YEAR'] >= start]
        return stats_in_range.set_index("YEAR")[stat]


    def graph_stats(self, stat, start, end):
        stats = self.get_stats(stat, start, end)
        ax = stats.plot()
        ax.legend([self.teamname + ' ' + stat]);


'''Available player stats:
    PLAYER_ID, SEASON_ID, LEAGUE_ID, TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE,
    GP, GS, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB,
    DREB, REB, AST, STL, BLK, TOV, PF, PTS'''

class Player:

    def __init__(self, name):
        self.search_name = name
        self.player = players.find_players_by_full_name(self.search_name)[0]
        self.playerid = self.player['id']
        self.playername = self.player['full_name']
        self.playerstats = playercareerstats.PlayerCareerStats(self.playerid).get_data_frames()[0]

    def get_stats(self, stat, start, end):
        stats_in_range = self.playerstats[self.playerstats['SEASON_ID'] <= end]
        stats_in_range = stats_in_range[self.playerstats['SEASON_ID'] >= start]
        return stats_in_range.set_index("SEASON_ID")[stat]

    def graph_stats(self, stat, start, end):
        stats = self.get_stats(stat, start, end)
        ax = stats.plot()
        ax.legend([self.playername + ' ' + stat]);








