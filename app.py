from flask import Flask, request, jsonify, Response
import pyodbc
from collections import OrderedDict
import json
from datetime import datetime


app = Flask(__name__)

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'
        'DATABASE=________________;'      # Provide the database name
        'UID=________________;'           # Provide username
        'PWD=________________;'           # Provide Password
    )
    return conn


# Custom JSON Encoder to handle datetime serialization
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string
        return super().default(obj)
 

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('userid', type=int)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if user_id is None:
        # Fetch all users if no userid is provided
        cursor.execute('SELECT * FROM UserTable')
        rows = cursor.fetchall()
        user = [OrderedDict(zip([column[0] for column in cursor.description], row)) for row in rows]
    else:
        # Fetch a specific user by userid
        cursor.execute('SELECT * FROM UserTable WHERE userid = ?', (user_id,))
        row = cursor.fetchone()
        if row is None:
            cursor.close()
            conn.close()
            return jsonify({'message': 'User not found'}), 404
        user = OrderedDict(zip([column[0] for column in cursor.description], row))

    cursor.close()
    conn.close()
    
    return Response(json.dumps(user, cls=CustomJSONEncoder), mimetype='application/json')


@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO UserTable (username, email, password_hash) VALUES (?, ?, ?)', (new_user['username'], new_user['email'], new_user['password_hash']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_user), 201


@app.route('/user', methods=['PUT'])
def update_user():
    user_id = request.args.get('userid', type=int)
    updated_user = request.json
    
    if user_id is None:
        return jsonify({'message': 'userid is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE UserTable SET username = ?, email = ?, password_hash = ? WHERE userid = ?',
                   (updated_user['username'], updated_user['email'], updated_user['password_hash'], user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_user)


@app.route('/user', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('userid', type=int)
    
    if user_id is None:
        return jsonify({'message': 'userid is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM UserTable WHERE userid = ?', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
