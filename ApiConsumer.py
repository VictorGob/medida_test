from datetime import datetime

import requests

from EventResponse import Event, EventsResponse
from eventsData import EventsData

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

    def get_data(self, events_data: EventsData) -> EventsResponse:
        try:
            team_rankings: dict = self.get_team_rankings(events_data.league)
            scoreboard: dict = self.get_scoreboard(
                events_data.league, events_data.startDate, events_data.endDate
            )
            return self.process_data(team_rankings, scoreboard)
        except Exception as e:
            raise ValueError({"error": str(e)})

    def get_team_rankings(self, league: str):
        url = self.url_team_rankings.format(league=league)
        response = requests.get(url)
        data = response.json()
        # User teamId as key, for faster lookup
        modified_data = {d.pop("teamId"): d for d in data}
        return modified_data

    def get_scoreboard(self, league: str, start_date: datetime, end_date: datetime):
        url = self.url_scoreboard.format(league=league)
        response = requests.get(
            url,
            params={"startDate": start_date.strftime("%Y-%m-%d"), "endDate": end_date.strftime("%Y-%m-%d")},
        )

        return response.json()

    def process_data(self, team_rankings: dict, scoreboard: dict) -> EventsResponse:
        # Process the data to generate the events
        events_response = EventsResponse(events=[])
        for score in scoreboard:
            datetime_obj = datetime.fromisoformat(score["timestamp"])
            event_date = datetime_obj.date()
            event_time = datetime_obj.time()
            homeTeamId = score["home"]["id"]
            awayTeamId = score["away"]["id"]
            event = Event(
                eventId=score["id"],
                eventDate=str(event_date),
                eventTime=str(event_time),
                # Home team
                homeTeamId=homeTeamId,
                homeTeamNickName=score["home"]["nickName"],
                homeTeamCity=score["home"]["city"],
                homeTeamRank=team_rankings[homeTeamId]["rank"],
                homeTeamRankPoints=team_rankings[homeTeamId]["rankPoints"],
                # Away team
                awayTeamId=awayTeamId,
                awayTeamNickName=score["away"]["nickName"],
                awayTeamCity=score["away"]["city"],
                awayTeamRank=team_rankings[awayTeamId]["rank"],
                awayTeamRankPoints=team_rankings[awayTeamId]["rankPoints"],
            )
            events_response.events.append(event)
        return events_response


"""Expected return:
```yaml
    Event: 
      type: object
      properties: 
        eventId: 
            type: string
            format: uuid
        eventDate: 
            type: string
            format: date
        eventTime: 
            type: string
            format: time
        homeTeamId: 
            type: string
            format: uuid
        homeTeamNickName: 
            type: string
        homeTeamCity: 
            type: string
        homeTeamRank:
            type: integer
            format: int64
            minimum: 1
        homeTeamRankPoints: 
            type: number
            format: float
            minimum: 0.0
        awayTeamId: 
            type: string
            format: uuid
        awayTeamNickName: 
            type: string
        awayTeamCity: 
            type: string
        awayTeamRank:
            type: integer
            format: int64
            minimum: 1
        awayTeamRankPoints: 
            type: number
            format: float
            minimum: 0.0
```
"""
