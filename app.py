from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_socketio import SocketIO
import pymysql
from flask_session import Session
from datetime import datetime, timedelta
import json
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
socketio = SocketIO(app)

db = pymysql.connect(host='db.default.svc.cluster.local',
                     user='doodle',
                     password='doodle',
                     database='doodle',
                     cursorclass=pymysql.cursors.DictCursor)


# Fonction pour récupérer les élèves depuis la base de données
def get_eleves():
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM eleve')
        eleves = cursor.fetchall()
    return eleves

@app.route('/')
def index():
    eleves = get_eleves()
    return render_template('index.html', eleves=eleves)

if __name__ == '__main__':
    socketio.run(app, debug=True)
