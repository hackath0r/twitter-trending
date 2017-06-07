import gevent
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from gevent import monkey

import config as cc
import twitter_helpers

INDIA_WOEID = cc.INDIA_WOEID

monkey.patch_all()

twitter_trending_app = Flask(__name__)
socketio = SocketIO(twitter_trending_app)

@twitter_trending_app.route('/')
def index():
    trends = twitter_helpers.get_trending_topics(INDIA_WOEID)
    return render_template('index.html', trends=trends)


if __name__ == '__main__':
    socketio.run(twitter_trending_app)
