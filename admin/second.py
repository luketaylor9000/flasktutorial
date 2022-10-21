from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/home")
@second.route("/")
def home():
  return render_template("admin_home.html")

@second.route("/admintest")
def test():
  return "<h1>'second' blueprint IS being shown because /admin url prefix is being used</h1>"