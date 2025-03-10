from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# เชื่อมต่อ MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['mydb']
collection = db['messages']

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Multi-Stage Flask App with MongoDB!"})

@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        collection.insert_one({"message": message})
        return jsonify({"message": f"Added '{message}' to MongoDB!"})
    return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)