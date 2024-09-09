from flask import Flask
from application.extensions import db, security
from application.create_initial_data import create_data


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
    db.init_app(app)
    app.app_context().push()
    with app.app_context():
        from application.models import User, Role
        from flask_security.datastore import SQLAlchemyUserDatastore
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        security.init_app(app, user_datastore)
        
        db.create_all()
        create_data(user_datastore)
        
    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
