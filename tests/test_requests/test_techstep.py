import requests
from pytest import mark


@mark.requests
def test_get_successful_response():
    resp = requests.get("http://techstepacademy.com/training-ground")
    print(resp.content)
