from flask import render_template
from flask_security.datastore import SQLAlchemyUserDatastore


def create_view(app, user_datastore: SQLAlchemyUserDatastore):

    @app.route('/')
    def home():
        return render_template('index.html')
