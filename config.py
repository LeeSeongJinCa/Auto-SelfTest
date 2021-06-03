import os


class User:
    name = os.getenv("USER_NAME")
    birth = os.getenv("USER_BIRTH")
    password = os.getenv("PASSWORD")
    org_code = os.getenv("ORG_CODE")