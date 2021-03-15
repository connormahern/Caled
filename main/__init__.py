from flask import Flask
from Flask_SQLAlchemy import SQLAlchemy
from flask_login import LoginManager
from main.config import configure_app
 


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
app = Flask( __name__ , instance_relative_config=True)
configure_app(app)

def create_app():
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @app.before_first_request
    def create_tables():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
