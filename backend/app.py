from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import controllers.Contact_controller as Contact_controller
import controllers.User_controller as User_controller
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)