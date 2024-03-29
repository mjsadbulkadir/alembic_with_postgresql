from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/example'
app.config['SECRET_KEY'] ='ThisIsSecretKey'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="users_detail"
    id = db.Column(db.Integer,primary_key = True)
    email =db.Column(db.String(50))
    user_name = db.Column(db.String(100))
    password = db.Column(db.Integer)
     
class Profile(db.Model):
    __tablename__="profile"
    id = db.Column(db.Integer,primary_key = True)
    email =db.Column(db.String(50))
    user_name = db.Column(db.String(100))
    password = db.Column(db.Integer)
     
class Contact(db.Model):
    __tablename__="contact"
    id = db.Column(db.Integer,primary_key = True)
    email =db.Column(db.String(50))
    user_name = db.Column(db.String(100))
    password = db.Column(db.Integer)
     
if __name__ == "__main__":
     app.run(debug=True,port=8000,use_reloader = False)
     