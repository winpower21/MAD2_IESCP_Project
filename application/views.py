from flask import render_template_string, request, jsonify
from flask_security.decorators import auth_required, roles_accepted, roles_accepted
from flask_login import current_user
from flask_security.utils import hash_password, verify_password
from flask import render_template, render_template_string
from flask_security.datastore import SQLAlchemyUserDatastore


def create_view(app, user_datastore: SQLAlchemyUserDatastore):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/user-login', methods=["POST"])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email or password not provided'}), 404

        user = user_datastore.find_user(email=email)

        if not user:
            return jsonify({'message': 'Invalid email'}), 404

        if verify_password(password, user.password):
            return jsonify({'token': user.get_auth_token(), 'user': user.email, 'role': user.roles[0].name}), 200
        else:
            return jsonify({'message': 'Incorrect password'}), 404

    @app.route('/influencer-dash')
    @roles_accepted('Influencer')
    def influencerDash():
        return render_template_string("<h1>This is Influencer Dashboard</h1>")

    @app.route('/admin-dash')
    @roles_accepted('Admin')
    def adminDash():
        return render_template_string("<h1>This is Admin Dashboard</h1>")

    @app.route('/sponsor-dash')
    @roles_accepted('Sponsor')
    def sponsorDash():
        return render_template_string("<h1>This is Sponsor Dashboard</h1>")
