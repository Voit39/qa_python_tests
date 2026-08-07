import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_users_1(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert type(data["name"]) == str


def test_get_users_2(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200 
    data = response.json()
    assert data["id"] == 2
    assert type(data["name"]) == str
    