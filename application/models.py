from application.database import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usersname = db.Column(db.String, unique=True, nullable=False)
    email = db.Comumn(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    influencer_id = db.relationship(
        'Influencers',  cascade='all,delete', backref='users')
    sponsor_id = db.relationship(
        'Sponsors',  cascade='all,delete', backref='users')


class Influencers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    facebook = db.Column(db.String, unique=True)
    instagram = db.Column(db.String, unique=True)
    youtube = db.Column(db.String, unique=True)
    x = db.Column(db.String, unique=True)
    threads = db.Column(db.String, unique=True)


class Spoonsors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False, unique=True)
    industry = db.Column(db.String, nullable=False)
    s_campaign = db.relationship(
        'Campaign', cascade='all,delete', backref='sponsors')
    s_adrequest = db.relationship(
        'AdRequest', cascade='all,delete', backref='sponsors')


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


class AdRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.id'))
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsors.id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    messages = db.Column(db.String, nullable=True)
    requirements = db.Column(db.String, nullable=True)
    payment_amt = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default='Pending')
