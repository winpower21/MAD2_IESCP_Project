from flask import session
from models import db, Roles, Users

def create_roles():
    if Roles.query.count() == 0:
        admin = Roles(name='Admin')
        sponsor = Roles(name='Sponsor')
        influencer = Roles(name='Influencer')

        db.session.add(admin)
        db.session.add(sponsor)
        db.session.add(influencer)

        db.session.commit()
        print('Roles successfully created!!!')
    else:
        print("Roles already exist!!!")
        
def create_admin():
    flag = Users.query.filter(Users.username == "").count()
