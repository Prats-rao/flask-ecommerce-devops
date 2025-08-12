from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Product
from .database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('main.index'))

@main.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    products = Product.query.filter(Product.id.in_(cart)).all()
    total = sum(p.price for p in products)
    return f"Checkout complete! Total: ${total:.2f}"
