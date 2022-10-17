#IMPORTS
from flask           import Flask, render_template
from flask_socketio  import SocketIO, send

#INIT FLASK && SOCKET_IO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socket_IO = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socket_IO.on('message')
def on_message(msg):
    print(f"el mensaje es : {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    socket_IO.run(app, host='0.0.0.0', port=5000, debug=True)