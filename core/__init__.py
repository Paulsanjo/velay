from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from .config import DevelopConfig
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(DevelopConfig)
CORS(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
admin = Admin(app, template_mode="bootstrap3")

from .models import (Customer, Review, Vendor,
                     Product, Sales, Order, Category)

admin.add_view(ModelView(Customer, db.session))
admin.add_view(ModelView(Vendor, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Review, db.session))
admin.add_view(ModelView(Sales, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Category, db.session))


from apis_routes.home import home
from apis_routes.vendor import vendor
from apis_routes.customer import customer

app.register_blueprint(home)
app.register_blueprint(vendor)
app.register_blueprint(customer)
