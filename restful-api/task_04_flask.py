#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(users)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def name(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add():
    data = request.get_json()

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if username in users:
        return jsonify({"message": "User already exists"}), 400

    users[username] = {
        'name': name,
        'age': age,
        'city': city
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
