from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        conn = mysql.connector.connect(
            host="database",
            user="root",
            password="password",
            database="orders_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = [{"id": row[0], "product_id": row[1], "user_id": row[2]} for row in cursor.fetchall()]
        conn.close()
        return jsonify(orders)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # รอ MySQL พร้อม
    time.sleep(10)
    app.run(host='0.0.0.0', port=5003)