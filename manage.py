from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.models import User, Post

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