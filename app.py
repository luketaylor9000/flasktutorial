from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
  return render_template("index.html", content="Testing")

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    user = request.form["nm"]
    session["user"] = user
    flash("Login successful!")
    return redirect(url_for("user"))
  else:
    if "user" in session:
      flash("Already logged in!")
      return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
  if "user" in session:
    user = session["user"]
    return render_template("user.html", user=user)
  else:
    flash("You are not logged in!")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
  if "user" in session:
    user = session["user"]
    flash(f"You have been logged out, {user}!", "info")
  else:
    flash("You are currently logged out")
  session.pop("user", None)
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)