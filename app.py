from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Product, Warehouse, Supplier, Stock, Transaction
from models import db, User, Product, Warehouse, Supplier, Stock, Transaction, Vehicle, Driver, ShipmentRoute

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enterprise_supply_chain.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def dashboard():
    total_products = Product.query.count()
    total_warehouses = Warehouse.query.count()
    total_suppliers = Supplier.query.count()
    transactions_count = Transaction.query.count()
    recent_transactions = Transaction.query.order_by(Transaction.id.desc()).limit(5).all()

    return render_template(
        'dashboard.html',
        total_products=total_products,
        total_warehouses=total_warehouses,
        total_suppliers=total_suppliers,
        t_count=transactions_count,
        transactions=recent_transactions
    )


@app.route('/products')
def list_products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/vehicles')
def list_vehicles():
    vehicles = Vehicle.query.all()
    drivers = Driver.query.all()
    return render_template('vehicles.html', vehicles=vehicles, drivers=drivers)


@app.route('/routes')
def list_routes():
    routes = ShipmentRoute.query.all()
    return render_template('routes.html', routes=routes)


if __name__ == '__main__':
    app.run(debug=True)
