from flask import Blueprint, render_template, request

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["GET"])
def register_form():
    return render_template("register.html")
