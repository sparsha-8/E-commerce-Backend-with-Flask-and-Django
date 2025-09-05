from flask import Blueprint, render_template, jsonify
from models import Order

order_bp = Blueprint("order", __name__, url_prefix="/orders")

@order_bp.route("/", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return render_template("orders.html", orders=orders)
