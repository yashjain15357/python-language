from flask import Flask , render_template , redirect,session, request,url_for , Response

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

# @app.route("/welcome")
# def welcome():
#     return render_template('welcome.html')
    