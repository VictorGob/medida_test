from fastapi import FastAPI
from fastapi.responses import JSONResponse

from ACMEsports.ApiConsumer import ApiConsumer
from ACMEsports.customErrors import RemoteAPIException
from ACMEsports.EventResponse import EventsResponse
from ACMEsports.eventsData import EventsData

app = FastAPI()


@app.post("/events")
async def get_events(data: EventsData):
    _resp: EventsResponse = ApiConsumer().get_data(data)
    return _resp


@app.exception_handler(RemoteAPIException)
async def validation_exception_handler(request, exc: RemoteAPIException):
    return JSONResponse(status_code=400, content={"message": exc.message})
