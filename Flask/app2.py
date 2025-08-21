from flask import Flask, redirect, request , Response , url_for, session
app= Flask(__name__)
app.secret_key = "supersecrate"


@app.route("/" , methods=["GET" , "POST"])
def Login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "yash" and password == "15357":
            session["ur"] = username
            return redirect(url_for("wellcome"))
        else:
            return Response("wrong username and password")
        
    return '''
    <h2>Login Page</h2>
    <form method="POST">
        username: <input type="text" name="username"> <br>
        password: <input type="password" name="password"> <br>
        <input type="submit" value="Login">
    </form>
    '''

    

@app.route("/wellcome")
def wellcome():
    if "ur" in session:
        return f'''
            <h2>WELLCOME, {session["ur"]}</h2>
            <a href={url_for('logout')}>Logout</a>
        '''
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("ur",None)
    return redirect(url_for("Login"))
