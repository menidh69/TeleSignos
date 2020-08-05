import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default') 
manager = Manager(app)
migrate = Migrate(app, db)

# app.config.from_object(os.environ['APP_SETTINGS'])

def make_shell_context():
    return dict(app=app, db=db, Usuario=Usuario, Tipo_Usuario=Tipo_Usuario)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()