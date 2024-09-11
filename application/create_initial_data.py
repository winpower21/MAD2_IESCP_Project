from flask_security.datastore import SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from application.extensions import db


def create_data(user_datastore: SQLAlchemyUserDatastore):
    print("--- Creaiting Data ---")

    user_datastore.find_or_create_role(name="Admin")
    user_datastore.find_or_create_role(name="Sponsor")
    user_datastore.find_or_create_role(name="Influencer")

    if not user_datastore.find_user(email="admin@platform.com"):
        user_datastore.create_user(username="Admin", email="admin@platform.com",
                                   password=hash_password("admin"), active=True, roles=['Admin'])
    if not user_datastore.find_user(email="sponsor@platform.com"):
        user_datastore.create_user(username="TestSponsor", email="sponsor@platform.com",
                                   password=hash_password("sponsor"), active=True, roles=['Sponsor'])
    if not user_datastore.find_user(email="influencer@platform.com"):
        user_datastore.create_user(username="TestInfluencer", email="influencer@platform.com",
                                   password=hash_password("influencer"), active=True, roles=['Influencer'])

    db.session.commit()

    print("--- Data Created ---")
