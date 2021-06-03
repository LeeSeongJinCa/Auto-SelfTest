import requests


class GetStudentAPI:
    uri = "https://djehcs.eduro.go.kr/v2/findUser"
    @staticmethod
    def get_student(encoded_name, encoded_birth, org_code):
        response = requests.post(GetStudentAPI.uri, json={
            "birthday": encoded_birth,
            "loginType": "school",
            "name": encoded_name,
            "orgCode": org_code,
            "stdntPNo": None
        })

        if response.status_code != 200:
            raise Exception("로그인 실패! 이름, 생일, 학교 코드를 확인해주세요")

        return response.json()["token"]
