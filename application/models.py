from application.extensions import db
from flask_security.core import UserMixin, RoleMixin
from flask_security.models import fsqla_v3 as fsq

fsq.FsModels.set_db_info(db)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    fs_uniquifier = db.Column(db.String)
    roles = db.relationship('Role', secondary='user_roles')  # type: ignore
    i_id = db.relationship(
        'Influencers', cascade='all,delete', backref='user')
    s_id = db.relationship('Sponsors', cascade='all,delete', backref='user')


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class Sponsors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String, nullable=False, unique=True)
    industry = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    c_id = db.relationship(
        'Campaigns', cascade='all,delete', backref='sponsors')


class Influencers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"))
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
    job_id = db.relationship(
        'Jobs', cascade='all,delete', backref='influencers')


class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s_id = db.Column(db.Integer, db.ForeignKey("sponsors.id"))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.String, nullable=False)
    goals = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    ad_request = db.relationship(
        'AdRequests', cascade='all,delete', backref='campaigns')


class AdRequests(db.Model):
    __tablename__ = 'adrequests'
    id = db.Column(db.Integer, primary_key=True)
    c_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
    messages = db.Column(db.String, nullable=True)
    requirements = db.Column(db.String, nullable=True)
    payment_amt = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default="Pending")
    job_id = db.relationship(
        'Jobs', cascade='all,delete', backref='adrequests')


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('adrequests.id'))
    i_id = db.Column(db.Integer, db.ForeignKey('influencers.id'))
