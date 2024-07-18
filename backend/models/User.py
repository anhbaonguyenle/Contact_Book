from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    User_name = db.Column(db.String(100), primary_key=True)
    User_password = db.Column(db.String(100), nullable = False)
    User_email = db.Column(db.String(100))
    User_phone = db.Column(db.String(15))
    User_gender = db.Column(db.String(6))
    User_img_url = db.Column(db.String(100))

    def set_password(self, password):
        self.User_password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.User_password, password)

    def to_json(self):
        return {
            'User_name': self.User_name,
            'User_email': self.User_email,
            'User_phone': self.User_phone,
            'User_gender' : self.User_gender,
            'User_img_url': self.User_img_url
        }
    
