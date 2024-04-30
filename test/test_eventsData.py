import pytest
from pydantic import ValidationError

from ACMEsports.eventsData import EventsData


def test_valid_data():
    # Valid data
    valid_data = {"league": "NFL", "startDate": "2024-05-01", "endDate": "2024-05-10"}
    # Ensure no ValidationError is raised
    EventsData(**valid_data)


def test_invalid_league():
    # Invalid league
    invalid_data = {
        "league": "NBA",  # Not a valid league
        "startDate": "2024-05-01",
        "endDate": "2024-05-10",
    }
    # Ensure a ValidationError is raised with the expected message
    with pytest.raises(ValidationError) as exc_info:
        EventsData(**invalid_data)
    assert "Value error, League must be one of" in exc_info.value.errors()[0]["msg"]


def test_invalid_date_format():
    # Invalid date format
    invalid_data = {
        "league": "NFL",
        "startDate": "2024/05/01",  # Invalid format
        "endDate": "2024-05-10",
    }
    # Ensure a ValidationError is raised with the expected message
    with pytest.raises(ValidationError) as exc_info:
        EventsData(**invalid_data)
    assert exc_info.value.errors()[0]["msg"] == "Value error, Start date must be in the format 'YYYY-MM-DD'"


def test_end_date_before_start_date():
    # End date before start date
    invalid_data = {
        "league": "NFL",
        "startDate": "2024-05-10",
        "endDate": "2024-05-01",  # End date is before start date
    }
    # Ensure a ValidationError is raised with the expected message
    with pytest.raises(ValidationError) as exc_info:
        EventsData(**invalid_data)
    assert exc_info.value.errors()[0]["msg"] == "Value error, End date must be after the start date"
