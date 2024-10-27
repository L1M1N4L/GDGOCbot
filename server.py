from flask import Flask
app = Flask(__name__)

@app.route('/send_message')
def send_message():
    # You can send the message to the Discord bot here
    return '', 204

if __name__ == '__main__':
    host = 'localhost'
    port = 3000
    app.run(debug=True)
    print(f'Server running at http://{host}:{port}')
