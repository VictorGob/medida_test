from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
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


# Exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(content={"detail": "Validation error occurred"}, status_code=400)


@app.exception_handler(RemoteAPIException)
async def remote_api_handler(request, exc: RemoteAPIException):
    return JSONResponse(status_code=400, content={"message": exc.message})
