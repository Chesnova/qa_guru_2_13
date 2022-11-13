from pprint import pprint
import requests
from requests import Response
from pytest_voluptuous import S
from schemas import schemas

def test_get():
    response: Response = requests.get(
        url='https://reqres.in/api/users',
        params={'page': 2},
        headers={'Autorization': 'token'},
        data={"a": "b"}
    )
    # print(response.status_code)
    pprint(response.request.headers)
    assert response.status_code == 200
    assert response.json()['page'] == 2
    assert len(response.json()['data']) != 0


def test_unknown_list_schema(reqres_session):
    result = reqres_session.get('/api/unknown')

    assert result.json() == S(schemas.unknown_list_schema)
    assert result.json()['data'][2]['id'] == 3


def test_delete(reqres_session):
    result = reqres_session.delete('/api/users/2')
    assert result.status_code == 204
    assert result.text == ''