from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from instance.config import app_config
from flask_migrate import Migrate
import os



db = SQLAlchemy()
app = Flask(__name__)

# init SQLAlchemy so we can use it later in our models
def create_app(config_name):
    
    app = Flask( __name__ , instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    app.config['SECRET_KEY'] = b'\xe0\xc3\x98\xdbH\xbd\x12E\xc4u\x84c\xfb\x1f\xa1h'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app)
    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
