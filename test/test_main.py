import pytest
from fastapi.testclient import TestClient

from ACMEsports.main import app

client = TestClient(app)


def test_get_events_wrong_method():
    response = client.get("/events")
    assert response.status_code == 405, "Should return 405 status code"
    response = client.options("/events")
    assert response.status_code == 405, "Should return 405 status code"
    response = client.put("/events")
    assert response.status_code == 405, "Should return 405 status code"
    # Test with POST method, no data
    response = client.post("/events")
    assert response.status_code == 400, "Should return 422 status code"


test_data = [
    ({"league": "NFL", "startDate": "2024-04-01", "endDate": "2024-04-30"}, 200),
    ({"league": "NFL", "startDate": "2024-04-01", "endDate": "2024-03-30"}, 400),
    ({"league": "XXX", "startDate": "2024-04-01", "endDate": "2024-04-30"}, 400),
]


@pytest.mark.parametrize("input_data, expected_status_code", test_data)
def test_get_events_wrong_data(input_data, expected_status_code):
    # Test with POST method, 1 with correct data, 2 with wrong data

    response = client.post("/events", json=input_data)
    assert response.status_code == expected_status_code, "Should return 400 status code"
