import os
from dotenv import load_dotenv

load_dotenv()

URL_BASE = 'https://as-academy-shop.vercel.app/'

USERNAME = os.getenv('APP_USERNAME')

PASSWORD = os.getenv('APP_PASSWORD')