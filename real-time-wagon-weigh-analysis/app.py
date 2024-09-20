from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from firebase_admin import credentials, firestore, initialize_app
import eventlet
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Firebase setup
cred = credentials.Certificate('config/firestore-api.json')
initialize_app(cred)
db = firestore.client()
iot_data_ref = db.collection('recorded_data')

# Function to classify wagon based on weight
def classify_wagon(weight):
    if weight < 800:
        return 'Underweight'
    elif 800 <= weight <= 900:
        return 'Normal'
    else:
        return 'Overweight'

# Handle incoming WebSocket messages from ESP8266
@socketio.on('sensor_data')
def handle_sensor_data(json_data):
    # Process incoming sensor data from ESP8266
    latitude = json_data['latitude']
    longitude = json_data['longitude']
    weight = json_data['weight']
    timestamp = datetime.utcnow()

    # Classify the wagon based on the weight
    category = classify_wwagon(weight)

    # Create a dictionary for the Firestore data
    data = {
        'latitude': latitude,
        'longitude': longitude,
        'weight': weight,
        'timestamp': timestamp,
        'category': category  # Store classification in Firestore
    }
    
    # Store data in Firestore
    iot_data_ref.add(data)

    # Send the sensor data to all connected clients (web browser)
    socketio.emit('update_data', data)

@app.route('/')
def index():
    return render_templ
