import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from config import Config, DevelopmentConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

cfg = '{}{}'.format(os.environ.get('FLASK_CONFIG').capitalize(), 'Config')

app = Flask(__name__)
app.config.from_object(eval(cfg))
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

from app import routes, models, errors
    
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    if os.environ.get('FLASK_CONFIG').lower() == 'production':
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (auth.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@{}'.format(app.config['MAIL_SERVER']),
                toaddrs=app.config['ADMINS'],
                subject='Microblog Failure',
                credentials=auth,
                secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)