from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

db_config = {
    'host': os.environ.get('DB_HOST', 'db'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'rootpassword'),
    'database': os.environ.get('DB_NAME', 'mydatabase')
}

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.json['data']
        cursor.execute("INSERT INTO items (data) VALUES (%s)", (data,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Data added successfully"}), 201

    elif request.method == 'GET':
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
