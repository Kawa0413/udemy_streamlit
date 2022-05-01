import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("subscription_key") # 環境変数の値をAPに代入
ENDPOINT = os.environ.get("endpoint")