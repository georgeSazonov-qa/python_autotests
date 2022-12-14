from urllib import response
import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/269')
    assert response.status_code == 200


def test_validname():
    response = requests.get('https://petstore.swagger.io/v2/pet/269')
    assert response.json()['name'] == 'Lumina'