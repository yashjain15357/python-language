from flask import Flask, url_for, redirect, render_template, session, request, flash
from form import RegForm

app = Flask(__name__)
app.secret_key = "flask_wtf"

@app.route("/" , methods = ["GET" , "POST"])
def regForm():
    form = RegForm()
    if form.validate_on_submit(): 
        name = form.name.data
        email = form.name.data
        flash(f"welcome {name} ")
        flash(f"thankyou for Registration")
        return redirect(url_for("success"))
    return render_template("register.html" , form=form)

@app.route("/success")
def success():
    return render_template("success.html")