import os
from flask import Flask
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import codes
    app.register_blueprint(codes.bp)
    app.add_url_rule('/', methods=('GET', 'POST'), endpoint='auth.login')

    return app
