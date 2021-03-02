from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://apecskaam:apecs123@apecs.gucd9.mongodb.net/APECS_User_Data?retryWrites=true&w=majority"
mongo=PyMongo(app)

@app.route('/')
def hello_world():
    return render_template('welcome.html')

"""@app.route('/error')
def error():
    return render_template('error_landing.html')"""

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['email']
      password=request.form['password']
      if(password==""):
         return render_template("signlog.html")

      a=mongo.db.Log_Sign_Data.find_one({'email':user})
      if (a==None):
          return render_template("error.html",message="Wrong UserId",toast="ERROR")
      elif(a['email']==user and a['password']==password):
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
      if(password=="" or name==""):
         return render_template("error.html",message="Enter all details",toast="OOPS!")
      a=mongo.db.Log_Sign_Data.find_one({'email':user})
      if(a==None):
         mongo.db.Log_Sign_Data.insert_one({'name':name,'email':user,'password':password})
         return redirect(url_for('login'))
      else:
         return render_template("error.html",message="We can see the email is already registered for APECS.",toast="ERROR")
   else:
      return render_template("sign.html")


if __name__=="__main__":
    app.run(debug=True)
