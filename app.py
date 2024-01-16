from flask import Flask, redirect
from database import db, connect_db, Temp
import serial
import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:3416SbSp13MS@localhost/arduino"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    ser = serial.Serial('COM3', 9600, timeout=1)

    print("Reading data from serial port...")
    time.sleep(2)
    ser.reset_input_buffer()

    for i in range (0, 7):
        line = ser.readline()
        print(str(line))
        time.sleep(0.5)

        if line:
            temp = Temp(temperature=line)

            db.session.add(temp)
            db.session.commit()
    # temp = Temp("10")

    # db.session.add(temp)
    # db.session.commit()
    print("Exit")

    return redirect("/")