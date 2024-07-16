from app import db,app
from flask import request, jsonify
from models import Contact

@app.route('/')
def home():
    return "Hello, Flask!"
# Select all
@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        contacts_json = [contact.to_json() for contact in contacts]
        return jsonify(contacts_json)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Create
@app.route("/api/contacts", methods=["POST"])
def create_contact():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input, no JSON provided'}), 400

        name = data.get('Contact_name')
        email = data.get('Contact_email')
        phone = data.get('Contact_phone')
        gender = data.get('Contact_gender')

        if not name:
            return jsonify({'error': 'Contact_name is required'}), 400
        if not phone:
            return jsonify({'error': 'Contact_phone is required'}), 400

        img_url = None
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        
        new_contact = Contact(
            Contact_name=name, 
            Contact_email=email, 
            Contact_phone=phone, 
            Contact_gender=gender, 
            Contact_img_url=img_url
        )
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({'message': 'Contact created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
# Delete
@app.route("/api/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):
    try:
        contact = Contact.query.get(id)
        if contact is None:
            return jsonify({"error": "Contact not found"}), 404
        
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "Contact deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
  
# Update
@app.route("/api/contacts/<int:id>", methods=["PATCH"])
def update_contact(id):
    try:
        contact = Contact.query.get(id)
        if contact is None:
            return jsonify({"error": "Contact not found"}), 404
        
        data = request.get_json()

        contact.Contact_name = data.get("Contact_name", contact.Contact_name)
        contact.Contact_email = data.get("Contact_email", contact.Contact_email)
        contact.Contact_phone = data.get("Contact_phone", contact.Contact_phone)
        contact.Contact_gender = data.get("Contact_gender", contact.Contact_gender)

        # Update image URL based on gender if gender is updated
        if "Contact_name" in data or "Contact_gender" in data:
            if contact.Contact_gender == "male":
                contact.Contact_img_url = f"https://avatar.iran.liara.run/public/boy?username={contact.Contact_name}"
            elif contact.Contact_gender == "female":
                contact.Contact_img_url = f"https://avatar.iran.liara.run/public/girl?username={contact.Contact_name}"

        db.session.commit()
        return jsonify(contact.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
