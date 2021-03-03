from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route('/')
def main():
    """Entry point; the view for the main page"""
    mail = ["this is mail1", "this is mail2", "this is mail3", "this is mail4", "this is mail5"]
    inbox = '5'
    return render_template("1.html", mail=mail, inbox=inbox)
    #return 'hi'

if __name__ == "__main__":
    app.run(debug=True)