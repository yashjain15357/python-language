from flask import Flask , request
app = Flask(__name__)

@app.route("/")
# after use of route the down runction run for this route
def Home():
    # return is complusary
    return "hello this is my first app"
@app.route("/yash")
def yash():
    return "this is a page of yash jain"



# GET POST
@app.route("/submit", methods=["GET" ,"POST"])
def submit():    
    if request.method == "GET":
        return "this is submit get"
    else:
        return "this is post submit"


