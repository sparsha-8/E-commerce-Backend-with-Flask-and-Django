from app import create_app
from extensions import db
from models import User, Product, Order, OrderItem

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add sample data
    user = User(username="testuser", email="test@example.com")
    product1 = Product(name="Laptop", price=1000, stock=10)
    product2 = Product(name="Phone", price=500, stock=20)

    db.session.add_all([user, product1, product2])
    db.session.commit()

    print("✅ Database initialized with sample data!")
