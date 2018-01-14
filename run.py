from os.path import join, dirname
from app import app
from dotenv import load_dotenv
load_dotenv(join(dirname(__file__), '.env'))

if __name__ == '__main__':
    app.run()