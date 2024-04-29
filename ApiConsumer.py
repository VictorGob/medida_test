import requests

URL_SCOREBOARD = "http://localhost:9000/{league}/scoreboard"
"""
Parameters:
    - league: str (enum)
    - startDate: str (format: 'YYYY-MM-DD')
    - endDate: str (format: 'YYYY-MM-DD')
"""
URL_TEAM_RANKINGS = "http://localhost:9000/{league}/team-rankings"
"""
Parameters:
    - league: str (enum)
"""


class ApiConsumer:
    def __init__(self):
        self.url_scoreboard = URL_SCOREBOARD
        self.url_team_rankings = URL_TEAM_RANKINGS

    def get_data(self, data):
        try:
            pass
        except Exception as e:
            return {"error": str(e)}
