from fastapi import FastAPI

from ACMEsports.ApiConsumer import ApiConsumer
from ACMEsports.EventResponse import EventsResponse
from ACMEsports.eventsData import EventsData

app = FastAPI()


@app.post("/events")
async def get_events(data: EventsData):
    _resp: EventsResponse = ApiConsumer().get_data(data)
    return _resp
