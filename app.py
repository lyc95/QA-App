from flask import Flask
import config
from exts import db
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from models import UserModel
from flask_migrate import Migrate

app = Flask(__name__)
# bind config file
app.config.from_object(config)
# bind db with app
db.init_app(app)

migrate = Migrate(app, db)
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
