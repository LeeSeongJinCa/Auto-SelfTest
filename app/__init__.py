from app.api.get_student import GetStudentAPI
from app.api.get_token import GetTokenAPI
from app.api.survey import SurveyAPI
from app.util.rsa_encoder import RSAEncoder


class AutoSelfTest:
    def __init__(self, name, birth, org_code, password):
        self.name = name
        self.birth = birth
        self.org_code = org_code
        self.password = password

        self.encoder = RSAEncoder()

    def run(self):
        temp_token = GetStudentAPI.get_student(
            self.encoder.encode(self.name),
            self.encoder.encode(self.birth),
            self.org_code
        )
        token = GetTokenAPI.get_token(temp_token, self.encoder.encode(self.password))
        SurveyAPI.survey(token, self.name)
