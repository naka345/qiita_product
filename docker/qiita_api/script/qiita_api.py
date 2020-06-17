import requests
from requests_oauthlib import OAuth2Session
import urllib.parse
import json
import os

state = "aa17785d811bb1913ef54b0a7657de780defaa2a"

redirect_url = r"https://127.0.0.1:5000/"
test = "https://127.0.0.1:5000/"

class QiitaApi:
    BASE_API_URL = "https://qiita.com/api/v2/"
    HEADERS = {'content-type': 'application/json'}

    def __init__(self):
        CLIENT_ID = os.environ.get("qiita_client_id")
        CLIENT_SECRET = os.environ.get("qiita_client_secret")
        self.payload_template = {"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET}

    @staticmethod
    def define_scope(scope_array):
        return " ".join(scope_array)

    def call_authorization_url(self, scope=[]):
        auth_api = "oauth/authorize"
        authorization_base_url = f"{self.BASE_API_URL}{auth_api}"
        client_id = self.payload_template["client_id"]
        oauth = OAuth2Session(client_id, redirect_uri=redirect_url, scope=scope)
        authorization_url, state = oauth.authorization_url(authorization_base_url)
        #authorization_response = input('Enter the full callback URL>> ')
        print(authorization_url)
        print(state)
        return authorization_url, state

    def response_authorization_url(self, response_url):
        code = urllib.parse.parse_qsl(response_url)[0][1]
        return code

    def access_tokens(self, code):
        token_api = "access_tokens"
        token_url = f'{self.BASE_API_URL}{token_api}'
        access_payload = {**self.payload_template, **{"code": code}}

        post_request = requests.post(token_url, data=json.dumps(
            access_payload), headers=self.HEADERS)
        token = post_request.json()["token"]
        self.bearer_token = {'Authorization': f'Bearer {token}'}
        self.create_auth_header()

    def create_auth_header(self):
        self.auth_header = {**self.HEADERS, **self.bearer_token}

    def get_item(self):
        get_item_api = "authenticated_user/items"
        get_item_url = f'{self.BASE_API_URL}{get_item_api}'
        item = requests.get(get_item_url, headers=self.auth_header)
        return item

    def adjust_item(self, items, pick_up_keys=[]):
        pick_up_keys.extend(["id"])
        items_dict = {}
        for item in items.json():
            pick_up_dict = {key: item[key] for key in pick_up_keys if key in item}
            item_dict.update({item["id"]: pick_up_dict})
        return items_dict

    def post_item(self):
        item_api = "items"
        item_url = f"{self.BASE_API_URL}{item_api}"
        payload = {"title": "test", "body": "# api test",
                   "tags": [{"name": "python"}], "private": True}
        post_status = requests.post(item_url, data=json.dumps(payload), headers=self.auth_header)
        return post_status

    def patch_item(self, item_id):
        patch_item_api = f"items/{item_id}"
        patch_item_url = f"{self.BASE_API_URL}{patch_item_api}"
        payload = {"title": "test2", "body": "# api test2",
                   "tags": [{"name": "python"}], "private": True}
        patch_status = requests.patch(
            patch_item_url, data=json.dumps(payload), headers=self.auth_header)
        return patch_status

if __name__ == '__main__':
    api = QiitaApi()
    scope = ["read_qiita", "write_qiita"]
    url = api.call_authorization_url(scope=QiitaApi.define_scope(scope))
    code = api.response_authorization_url(url)
    api.access_tokens(code)
    items = api.get_item()
    pick_up_keys = ["title","url","body","private"]
    items_dict = api.adjust_item(items,pick_up_keys)
