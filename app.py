from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Product, Warehouse, Supplier, Stock, Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enterprise_supply_chain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    products_count = Product.query.count()
    warehouses_count = Warehouse.query.count()
    suppliers_count = Supplier.query.count()
    transactions_count = Transaction.query.count()
    recent_transactions = Transaction.query.order_by(Transaction.timestamp.desc()).limit(5).all()
    
    return render_template(
        'dashboard.html', 
        p_count=products_count, 
        w_count=warehouses_count, 
        s_count=suppliers_count,
        t_count=transactions_count,
        transactions=recent_transactions
    )

@app.route('/products')
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
