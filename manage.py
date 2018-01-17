from os.path import join, dirname
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from app import create_app, db
from app.models import User, Post
load_dotenv(join(dirname(__file__), '.env'))

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.shell
def shell():
    return {
        'app': app,
        'db': db,
        'User': User,
        'Post': Post
    }


if __name__ == '__main__':
    manager.run()
