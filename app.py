from flask import Flask
from extensions import db
from models import User, Product, Order, OrderItem
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp
from routes.order_routes import order_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register routes
    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(order_bp, url_prefix="/orders")

    @app.route("/")  # homepage
    def home():
        return "Welcome to the E-commerce App! Go to /products, /auth/register, or /orders."

    return app


# ✅ this part is required to actually run the server
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
