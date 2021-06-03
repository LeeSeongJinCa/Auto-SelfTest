import requests


class SurveyAPI:
    uri = "https://djehcs.eduro.go.kr/registerServey"

    @staticmethod
    def survey(token, name):
        response = requests.post(SurveyAPI.uri, json={
            "deviceUuid": "",
            "rspns00": "Y",
            "rspns01": "1",
            "rspns02": "1",
            "rspns03": None,
            "rspns04": None,
            "rspns05": None,
            "rspns06": None,
            "rspns07": None,
            "rspns08": None,
            "rspns09": "0",
            "rspns10": None,
            "rspns11": None,
            "rspns12": None,
            "rspns13": None,
            "rspns14": None,
            "rspns15": None,
            "upperToken": token,
            "upperUserNameEncpt": name
        }, headers={
            "Authorization": token
        })
