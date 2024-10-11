from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

def get_db_connection():
    conn = sqlite3.connect('db_data/faq.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/chat', methods=['GET'])
def chat():
    question = request.args.get('question')
    conn = get_db_connection()
    cursor = conn.execute("SELECT answer FROM faq WHERE question = ?", (question,))
    answer = cursor.fetchone()
    conn.close()
    
    if answer:
        return jsonify({'answer': answer['answer']})
    else:
        return jsonify({'answer': 'Sorry, I don’t know the answer to that question.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


