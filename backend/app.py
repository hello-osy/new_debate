from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL 연결 설정
db_config = {
    'host': 'db',
    'user': 'user',
    'password': 'password',
    'database': 'mydatabase'
}

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/data')
def get_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sample_table")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
