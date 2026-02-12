import os
from dotenv import load_dotenv
from YougileApi import YougileApi

load_dotenv()

api = YougileApi("https://ru.yougile.com")


# позитивный тест на изменение названия проекта
def test_positive_change_project():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    result = api.get_id(login, password)
    company_id = result.json()["content"][0]["id"]
    assert result.status_code == 200
    assert result.json()["content"][0]["id"] == company_id

    result = api.create_key(login, password, company_id)
    auth_key = result.json()['key']
    assert result.status_code == 201
    assert result.json()['key'] == auth_key

    name_project = "QA Engineer"
    result = api.create_project(auth_key, name_project)
    project_id = result.json()["id"]
    assert result.status_code == 201
    assert result.json()["id"] == project_id

    result = api.get_project_by_id(auth_key, project_id)
    assert result.json()["title"] == name_project
    assert result.json()["id"] == project_id
    assert result.status_code == 200

    name_change_project = "Top QA Engineer"
    result = api.change_project(auth_key, project_id, name_change_project)
    assert result.status_code == 200
    assert result.json()["id"] == project_id

    result = api.get_list_project(auth_key)
    assert result.status_code == 200
    assert result.json()["content"][-1]["title"] == "Top QA Engineer"
    assert result.json()["content"][-1]["id"] == project_id

    result = api.delete_project(auth_key, project_id)
    assert result.status_code == 200
    assert result.json()["id"] == project_id

    result = api.delete_key(auth_key)
    assert result.status_code == 200
    assert result.json()["result"] == "ok"


# негативный тест на изменение названия проекта с пустым названием
def test_negative_change_project():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    result = api.get_id(login, password)
    company_id = result.json()["content"][0]["id"]
    assert result.status_code == 200
    assert result.json()["content"][0]["id"] == company_id

    result = api.create_key(login, password, company_id)
    auth_key = result.json()['key']
    assert result.status_code == 201
    assert result.json()['key'] == auth_key

    name_project = "QA Engineer"
    result = api.create_project(auth_key, name_project)
    project_id = result.json()["id"]
    assert result.status_code == 201
    assert result.json()["id"] == project_id

    result = api.get_project_by_id(auth_key, project_id)
    assert result.json()["title"] == name_project
    assert result.json()["id"] == project_id
    assert result.status_code == 200

    name_change_project = ""
    result = api.change_project(auth_key, project_id, name_change_project)
    assert result.status_code == 400
    assert result.json()['message'] == ['title should not be empty']
    assert result.json()['error'] == 'Bad Request'

    result = api.delete_project(auth_key, project_id)
    assert result.status_code == 200
    assert result.json()["id"] == project_id

    result = api.delete_key(auth_key)
    assert result.status_code == 200
    assert result.json()["result"] == "ok"
