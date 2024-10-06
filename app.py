from flask import Flask
from application.extensions import db, security
from application.create_initial_data import create_data
from application.views import create_view


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iescp.sqlite3'
    # needed for session cookies
    app.config['SECRET_KEY'] = 'MY_SECRET'
    # hashes the password and then stores in the database
    app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
    # allows new registrations to application
    app.config['SECURITY_REGISTERABLE'] = True
    # to send automatic registration email to user
    app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

    app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authentication-Token'
    app.config['SECURITY_TOKEN_MAX_AGE'] = 3600  # 1hr
    app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = True

    # cache config
    app.config["DEBUG"] = True         # some Flask specific configs

    db.init_app(app)
    with app.app_context():
        from application.models import User, Role
        from flask_security.datastore import SQLAlchemyUserDatastore

        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security.init_app(app, user_datastore)

        db.create_all()
        create_data(user_datastore)

    # disable CSRF security
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    app.config['SECURITY_CSRF_PROTECT_MECHANISHMS'] = []
    app.config['SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS'] = True

    create_view(app, user_datastore)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(port=8000)
