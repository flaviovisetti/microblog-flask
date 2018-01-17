import os
from app import create_app
from config import Config, DevelopmentConfig, ProductionConfig
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

cfg = '{}{}'.format(os.environ.get('FLASK_CONFIG').capitalize(), 'Config')
app = create_app(eval(cfg))

if __name__ == '__main__':
    app.run()
