from app import create_app
from app.database import db
from app.models import Product

app = create_app()

with app.app_context():
    if not Product.query.first():  # Only seed if no products exist
        sample_products = [
            Product(name="Samosa", price=1.50),
            Product(name="Chai", price=0.99),
            Product(name="Paneer Tikka", price=5.00),
            Product(name="Biryani", price=7.50)
        ]
        db.session.add_all(sample_products)
        db.session.commit()
        print("✅ Database seeded with sample products!")
    else:
        print("ℹ️ Products already exist, skipping seeding.")
