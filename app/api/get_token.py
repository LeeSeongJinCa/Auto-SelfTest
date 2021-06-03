import requests


class GetTokenAPI:
    uri = "https://djehcs.eduro.go.kr/v2/validatePassword"
    @staticmethod
    def get_token(token, encoded_password):
        response = requests.post(GetTokenAPI.uri, json={
            "deviceUuid":"",
            "password": encoded_password
        }, headers={
            "Authorization": token
        })

        if response.status_code != 200:
            raise Exception("로그인 실패! 비밀번호를 확인해주세요")

        return response.json()
