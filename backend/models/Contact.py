from app import db

class Contact(db.Model):
    Contact_id = db.Column(db.Integer, primary_key=True)
    Contact_name = db.Column(db.String(100), nullable = False)
    Contact_email = db.Column(db.String(100))
    Contact_phone = db.Column(db.String(15))
    Contact_gender = db.Column(db.String(6))
    Contact_img_url = db.Column(db.String(100))

    def to_json(self):
        return {
            'Contact_id': self.Contact_id,
            'Contact_name': self.Contact_name,
            'Contact_email': self.Contact_email,
            'Contact_phone': self.Contact_phone,
            'Contact_gender' : self.Contact_gender,
            'Contact_img_url': self.Contact_img_url
        }