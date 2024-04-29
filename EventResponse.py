from typing import List

from pydantic import UUID4, BaseModel


class Event(BaseModel):
    eventId: UUID4
    eventDate: str
    eventTime: str
    homeTeamId: UUID4
    homeTeamNickName: str
    homeTeamCity: str
    homeTeamRank: int
    homeTeamRankPoints: float
    awayTeamId: UUID4
    awayTeamNickName: str
    awayTeamCity: str
    awayTeamRank: int
    awayTeamRankPoints: float


class EventsResponse(BaseModel):
    events: List[Event]
