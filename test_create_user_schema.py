import requests
from pytest_voluptuous import S
from schemas import schemas


def test_create_user_schema(reqres_session):
    name = "Raul"
    job = "journalist"

    response = reqres_session.post(
        url='/api/users',
        json={
            "name": name,
            "job": job
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    # assert isinstance(response.json()['id'], str)
    assert response.json() == S(schemas.create_user_schema)


def test_update_user_schema(reqres_session):
    name = 'William'
    job = 'accountant'

    response = reqres_session.put(
        url='/api/users/2',
        json={
            "name": name,
            "job": job
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    assert response.json() == S(schemas.update_user_schema)


def test_delete_user(reqres_session):
    response = reqres_session.delete(url='/api/users/2')

    assert response.status_code == 204


def test_get_single_user(reqres_session):
    response = reqres_session.get(url='/api/users/2')

    assert response.status_code == 200
    assert response.json()["data"]
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert response.json()["data"]["first_name"] == "Janet"
    assert response.json()["data"]["last_name"] == "Weaver"
    assert response.json() == S(schemas.get_single_user_schema)


def test_successful_register_user(reqres_session):
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = reqres_session.post(
        url='/api/register',
        json={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json()["id"] == 4
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert response.json() == S(schemas.successful_register_user_schema)
