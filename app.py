from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Warehouse, Supplier, Stock

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supply_chain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    products_count = Product.query.count()
    warehouses_count = Warehouse.query.count()
    suppliers_count = Supplier.query.count()
    return render_template('dashboard.html', p_count=products_count, w_count=warehouses_count, s_count=suppliers_count)

@app.route('/products')
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
