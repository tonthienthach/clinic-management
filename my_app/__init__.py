from flask import  Flask
from  flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:01688948780thach@localhost/phongmachtu?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "!@#$%^&*()(*&^%$#@#$%^&*("

db=SQLAlchemy(app=app)
my_login=LoginManager(app=app)
