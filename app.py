from flask import Flask
from application.database import db

app = None


def create_app():
    global db, app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iescp.sqlite3'
    db.init_app(app)
    app.app_context().push()
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
