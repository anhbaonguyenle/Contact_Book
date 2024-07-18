from app import db, app
from flask import request, jsonify
from models.User import User

# Create
@app.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input, no JSON provided'}), 400

        username = data.get('User_name')
        password = data.get('User_password')
        email = data.get('User_email')
        phone = data.get('User_phone')
        gender = data.get('User_gender')

        if not username or not password:
            return jsonify({'error': 'User_name and User_password are required'}), 400

        img_url = None
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={username}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={username}"

        new_user = User(
            User_name=username, 
            User_email=email, 
            User_phone=phone, 
            User_gender=gender, 
            User_img_url=img_url
        )
        new_user.set_password(password) 

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get
@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        users_json = [user.to_json() for user in users]
        return jsonify(users_json)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a single user
@app.route("/api/users/<string:username>", methods=["GET"])
def get_user(username):
    try:
        user = User.query.get(username)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_json()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update
@app.route("/api/users/<string:username>", methods=["PATCH"])
def update_user(username):
    try:
        user = User.query.get(username)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()

        if 'User_password' in data:
            user.set_password(data['User_password'])
        user.User_email = data.get("User_email", user.User_email)
        user.User_phone = data.get("User_phone", user.User_phone)
        user.User_gender = data.get("User_gender", user.User_gender)

        if "User_name" in data or "User_gender" in data:
            if user.User_gender == "male":
                user.User_img_url = f"https://avatar.iran.liara.run/public/boy?username={user.User_name}"
            elif user.User_gender == "female":
                user.User_img_url = f"https://avatar.iran.liara.run/public/girl?username={user.User_name}"

        db.session.commit()
        return jsonify(user.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete
@app.route("/api/users/<string:username>", methods=["DELETE"])
def delete_user(username):
    try:
        user = User.query.get(username)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
