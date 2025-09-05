from flask import Blueprint, render_template
from models import Product

product_bp = Blueprint("product", __name__)

@product_bp.route("/")
def get_products():
    products = Product.query.all()
    return render_template("products.html", products=products)
