from flask import Flask, url_for, redirect, render_template, session, request, flash

app = Flask(__name__)

app.secret_key = "flash_message"

@app.route("/" ,methods = ["GET" ,"POST"])
def form():
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("enter you name, it not be empty")
            return redirect(url_for("form"))

        flash(f"thank you {name} , your feedback is saved")
        flash("i love riya and raksha ")
        return redirect(url_for("thankyou" ,username = name))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")