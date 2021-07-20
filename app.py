# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# import random
# #import string 
# import os



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///urls.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Urls(db.Model):
#     id_ = db.Column("id_", db.Integer, primary_key=True)
#     long = db.Column("long", db.String())
#     short = db.Column("short", db.String(3))

#     def __init__(self, long, short):
#         self.long = long
#         self.short = short

# @app.before_first_request
# def create_tables():
#     db.create_all()        

# @app.route('/', methods=['POST', 'GET'])
# def home():
#     if request.method == "POST":
#         url_received = request.form["nm"]
#         return url_received
#     else:
#         return render_template("home.html")    
            
# if __name__ == '__main__' :
#     app.run(port=5000, debug=True)

from flask import Flask  ,render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["nm"]
        return url_received
    else:
        return render_template('shorturl.html')    

if __name__ == '__main__' :
    app.run(port=5000,debug=True)