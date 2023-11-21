import pytest
import requests

@pytest.mark.https
def test_first_request():
    r1 = requests.get('https://api.github.com/zen')
    print(f'response is: {r1.text}')

@pytest.mark.https
def test_second_request():
    reques = requests.get('https://api.github.com/users/defunkt')
    namet = reques.json()
    head = reques.headers
    assert namet['name'] == 'Chris Wanstrath'
    assert reques.status_code == 200
    assert head['Server']== 'GitHub.com'

@pytest.mark.https
def test_status_code_request():
    request3 = requests.get('https://api.github.com/users/sergii_butenko')
    print(f'Responce status code is: {request3.status_code}')