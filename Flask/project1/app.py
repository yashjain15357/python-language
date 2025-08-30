from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")
        return render_template("thankyou.html", username=username, message=message)

    # For GET, use query parameters if present
    username = request.args.get("username", "")
    message = request.args.get("message", "")
    return render_template("feedback.html", username=username, message=message)

@app.route("/thankyou")
def func():
    return render_template("thankyou.html")