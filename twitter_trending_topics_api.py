import gevent
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from gevent import monkey

monkey.patch_all()

twitter_trending_app = Flask(__name__)
socketio = SocketIO(twitter_trending_app)

@twitter_trending_app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(twitter_trending_app)
