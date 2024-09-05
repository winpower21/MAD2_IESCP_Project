import enum
from application.database import db


class UserType(enum.Enum):
    admin = 0
    influencer = 1
    sponsor = 2


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usersname = db.Column(db.String, unique=True, nullable=False)
    email = db.Comumn(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    type = db.Column(db.ChoiceType(
        UserType, impl=db.Integer()), nullable=False)
    influencer_id = db.relationship(
        'Influencers',  cascade='all,delete', backref='users')
    sponsor_id = db.relationship(
        'Sponsors',  cascade='all,delete', backref='users')


class Influencers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    fName = db.Column(db.String(28), nullable=False)
    lName = db.Column(db.String(28), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(250), nullable=False)
    sector = db.Column(db.String, nullable=False)
    facebook = db.Column(db.String, unique=True)
    instagram = db.Column(db.String, unique=True)
    youtube = db.Column(db.String, unique=True)
    x = db.Column(db.String, unique=True)
    threads = db.Column(db.String, unique=True)


class Spoonsors(db.Model):
    CATEGORY = [
        ('individual', 'Individual'),
        ('company', 'Company')
    ]
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False, unique=True)
    industry = db.Column(db.String, nullable=False)
    category = db.Column(db.ChoiceType(CATEGORY), nullable=False)
    s_campaign = db.relationship(
        'Campaign', cascade='all,delete', backref='sponsors')
    s_adrequest = db.relationship(
        'AdRequests', cascade='all,delete', backref='sponsors')


class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sponsor_id = db.Column(db.String, db.ForeignKey('sponsors.id'))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.String, nullable=False)
    goals = db.Column(db.String, nullable=False)
    ad_requests = db.relationship(
        'AdRequests', cascade='all,delete', backref='sponsors')


class AdRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.id'))
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsors.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    messages = db.Column(db.String, nullable=True)
    requirements = db.Column(db.String, nullable=True)
    payment_amt = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default='Pending')
