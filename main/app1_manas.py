from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://apecskaam:apecs123@apecs.gucd9.mongodb.net/APECS_User_Data?retryWrites=true&w=majority"
mongo=PyMongo(app)

"""@app.route('/')
def hello_world():
    return render_template('Webmail.html')"""


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['email']
      #name=request.form['name']
      if user=="manasbedekar002@gmail.com":
          return render_template("1.html")
      else:
          return render_template("signlog.html")
   else:
      return render_template("signlog.html")

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      user = request.form['email']
      name=request.form['name']
      password=request.form['password']

      a=mongo.db.Log_Sign_Data.find_one({'name':name})
      print(a['email'])
      return redirect(url_for('login'))
   else:
      return render_template("sign.html")


if __name__=="__main__":
    app.run(debug=True)
