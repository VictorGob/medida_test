from fastapi import FastAPI

from ApiConsumer import ApiConsumer
from EventResponse import EventsResponse
from eventsData import EventsData

app = FastAPI()


@app.post("/events")
async def get_events(data: EventsData):
    _resp: EventsResponse = ApiConsumer().get_data(data)
    print(f"*** main: {_resp=} ***")
    # return {"message": "Event data received", "data": data.model_dump()}
    # return _resp.model_dump_json()
    return _resp
