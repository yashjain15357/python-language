from flask import Flask , render_template , redirect,session, request,url_for , Response
app = Flask(__name__)

@app.route("/")
def profile():
    return render_template("profile.html" ,
                           name="yash" , 
                           marks = 70, 
                           subject = ["maths","english" , "AI"])