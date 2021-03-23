import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from instance.config import app_config

from main import app , db

config_name = os.getenv('FLASK_CONFIG')
app.config.from_object(app_config[config_name])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()