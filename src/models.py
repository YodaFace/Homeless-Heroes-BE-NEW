from flask_sqlalchemy import SQLAlchemy

import enum
import datetime

db = SQLAlchemy()

class Homeless_User(db.Model):
    __tablename__ = 'homeless_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    currently_homless = db.Column(db.Boolean, unique=False, nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    story = db.Column(db.String(10000), unique=False, nullable=True)
    ## RELATIONSHIPS ## 
    primary_shelter = db.relationship('Shelter', backref='homeless_user', lazy=True)
    deposit = db.relationship('Deposit', backref='homeless_user', lazy=True)

    def __repr__(self):
        return '<Homeless_User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "joined": self.date_joined,
            "shelter": self.primary_shelter
        }


class Shelter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shelter_name = db.Column(db.String(80), unique=True, nullable=False)
    address_1 = db.Column(db.String(120), unique=False, nullable=False)
    address_2 = db.Column(db.String(120), unique=False, nullable=False)
    beds_available = db.Column(db.Boolean, unique=False, nullable=False)
    homeless_user_id = db.Column(db.Integer, db.ForeignKey ('homeless_user.id'), nullable=False)

    def serialize(self):
        return {
            "shelter_name": self.shelter_name,
            "email": self.email
        }

class Contributor (db.Model):
    __tablename__ = 'contributor'
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    number_of_contributions = db.Column(db.Integer, unique=False, nullable=True)
    donated_to_homeless_user = db.Column(db.Integer, db.ForeignKey ('homeless_user.id'), nullable=False)


class Deposit (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=True)
    homeless_user_id = db.Column(db.Integer, db.ForeignKey ('homeless_user.id'), nullable=False)
    contributor_user_id = db.Column(db.Integer, db.ForeignKey ('contributor.id'), nullable=False)


class Card (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    homeless_user_id = db.Column(db.Integer, db.ForeignKey ('homeless_user.id'), nullable=False)
    card_number = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.Float, nullable=True)
    transaction_pending = db.Column(db.Float, nullable=True)
    status = db.Column(db.Boolean, unique=False, nullable=False)
    daily_limit = db.Column(db.Float, nullable=True)




# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }