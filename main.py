from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class EventData(BaseModel):
    league: str
    startDate: datetime
    endDate: datetime

    @field_validator("league")
    @classmethod
    def validate_league(cls, v):
        # Check if the start date is in the correct format
        # TODO: get the valid leagues from yml schema
        valid_leagues = ["NFL"]
        if v not in valid_leagues:
            raise ValueError(f"League must be one of {valid_leagues}")
        return v

    @field_validator("startDate", mode="before")
    @classmethod
    def validate_start_date(cls, v):
        # Check if the start date is in the correct format, and transform it to datetime
        try:
            start_date = datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Start date must be in the format 'YYYY-MM-DD'")
        return start_date

    @field_validator("endDate", mode="before")
    @classmethod
    def validate_end_date(cls, v, values, **kwargs):
        # Check if the end date is in the correct format, and transform it to datetime
        try:
            end_date = datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("End date must be in the format 'YYYY-MM-DD'")

        # Check if the end date is after the start date
        if "startDate" in values.data and end_date <= values.data["startDate"]:
            raise ValueError("End date must be after the start date")
        return end_date


@app.post("/events")
async def get_events(data: EventData):
    return {"message": "Event data received", "data": data.model_dump()}
