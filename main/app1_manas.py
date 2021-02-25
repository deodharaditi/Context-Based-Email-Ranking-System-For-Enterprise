from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

"""@app.route('/')
def hello_world():
    return render_template('Webmail.html')"""


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['email']
      #name=request.form['name']
      if user=="manasbedekar002@gmail.com":
          return render_template("Webmail.html")
      else:
          return render_template("signlog.html")
   else:
      return render_template("signlog.html")

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      user = request.form['email']
      name=request.form['name']
      print(name)
      if user=="manasbedekar002@gmail.com":
          return render_template("Webmail.html")
      else:
          return render_template("sign.html")
   else:
      return render_template("sign.html")


if __name__=="__main__":
    app.run(debug=True)
