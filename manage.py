from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.post.models import Post


app = create_app('default')


def make_shell_context():
    return dict(app=app, db=db, Post=Post)


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
