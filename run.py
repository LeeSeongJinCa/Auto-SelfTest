from config import User
from app import AutoSelfTest

app = AutoSelfTest(User.name, User.birth, User.org_code, User.password)
print(User.name)
app.run()