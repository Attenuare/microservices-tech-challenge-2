from request_manager.manager import RequestManager
from dotenv import load_dotenv
import requests
import secrets
import sys
import os

load_dotenv()


class TestScriptTechChallenge():
    def __init__(self, users: int = 100):
        self.host = os.environ.get("EVALUTION_HOST")
        self.flag = os.environ.get("FLAG")
        self.users = users
    
    def generate_random_user(self) -> None:
        user_name = secrets.token_hex(8 // 2)
        user_name = f"user_{user_name}"
        return user_name

    def send_message(self) -> None:
        params = {"flag_name": self.flag, "user_id": self.generate_random_user()}
        print(f"[LOG] - Sending User {params['user_id']} | flag \
              {params['flag_name']}")
        response = requests.post(self.host, params=params)
        print(response.json())
    def run(self) -> None:
        for _ in range(self.users):
            self.send_message()



# users = int(sys.argv[1])
# TestScriptTechChallenge(users).run()

from concurrent.futures import ThreadPoolExecutor
import sys

users = int(sys.argv[1])
test = TestScriptTechChallenge(users)

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(lambda _: test.send_message(), range(users))