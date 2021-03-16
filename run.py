import os
from main import create_app

config_name = os.getenv('venv')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()