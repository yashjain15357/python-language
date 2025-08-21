from flask import Flask , redirect , request, render_template, Response, url_for
app = Flask(__name__)

@app.route("/" , methods=["POST" , "GET"])
def home():    
    return render_template("home.html")

@app.route("/submit" , methods=["POST" , "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        data ={
            "yash":"15357",
            "riya":"yash",
            "raksha":"love"
        }
        if username in data and password == data[username]:
            # session["user"] = username
            return render_template("welcome.html",name = username)
        else:
            return Response('''
        <h2>wrong username or password</h2>
''')
        
@app.route("/profile")
def profile():
    return render_template("profile.html" ,
                           name="yash" , 
                           marks = 70, 
                           subject = ["maths","english" , "AI"])