from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class EventData(BaseModel):
    league: str
    startDate: str
    endDate: str

    @field_validator("startDate")
    @classmethod
    def validate_start_date(cls, v):
        # Check if the start date is in the correct format
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Start date must be in the format 'YYYY-MM-DD'")
        return v

    @field_validator("endDate")
    @classmethod
    def validate_end_date(cls, v, values, **kwargs):
        # Check if the end date is in the correct format
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("End date must be in the format 'YYYY-MM-DD'")

        # Check if the end date is after the start date
        if "startDate" in values and v <= values["startDate"]:
            raise ValueError("End date must be after the start date")
        return v


@app.post("/events")
async def get_events(data: EventData):
    return {"message": "Event data received", "data": data.model_dump()}
