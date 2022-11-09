from pprint import pprint
import requests
from requests import Response


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