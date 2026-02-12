import requests


class YougileApi:

    def __init__(self, url):
        self.url = url

    def get_id(self, login, password, name=""):
        user_data = {
            'login': login,
            'password': password
        }
        response = requests.post(self.url + "/api-v2/auth/companies",
                                 json=user_data)
        return response

    def create_key(self, login, password, company_id):
        user_data = {
            'login': login,
            'password': password,
            'companyId': company_id
        }
        response = requests.post(self.url + "/api-v2/auth/keys",
                                 json=user_data)
        return response

    def create_project(self, auth_key, name_project):
        my_header = {
            'Authorization': 'Bearer ' + auth_key,
            'Content-Type': 'application/json'
        }
        data = {
            'title': name_project
        }
        response = requests.post(self.url + "/api-v2/projects",
                                 headers=my_header, json=data)
        return response

    def get_project_by_id(self, auth_key, project_id):
        my_header = {
            'Authorization': 'Bearer ' + auth_key,
            'Content-Type': 'application/json'
        }
        response = requests.get(self.url + "/api-v2/projects/"
                                + project_id, headers=my_header)
        return response

    def change_project(self, auth_key, project_id, title):
        my_header = {
            'Authorization': 'Bearer ' + auth_key,
            'Content-Type': 'application/json'
        }
        data = {
            "title": title
        }
        response = requests.put(self.url + "/api-v2/projects/"
                                + project_id, headers=my_header, json=data)
        return response

    def get_list_project(self, auth_key):
        my_header = {
            'Authorization': 'Bearer ' + auth_key,
            'Content-Type': 'application/json'
        }
        response = requests.get(self.url + "/api-v2/projects",
                                headers=my_header)
        return response

    def delete_project(self, auth_key, project_id):
        my_header = {
            'Authorization': 'Bearer ' + auth_key,
            'Content-Type': 'application/json'
        }
        data = {
            'deleted': True
        }
        response = requests.put(self.url + "/api-v2/projects/"
                                + project_id, headers=my_header, json=data)
        return response

    def delete_key(self, auth_key):
        response = requests.delete(self.url + "/api-v2/auth/keys/" + auth_key)
        return response
