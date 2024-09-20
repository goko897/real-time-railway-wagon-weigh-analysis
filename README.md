# IoT-based Wagon Weight Monitoring System 🚂

Our IoT-based Wagon Weight Monitoring System is designed to provide real-time monitoring of freight wagons' weight using advanced sensors that capture data like longitude, latitude, temperature, and weight. The sensor data is transmitted to a centralized system where it is stored securely in Google Firestore for further analysis and monitoring.

This system classifies wagons into three categories—**Overweight**, **Underweight**, and **Normal**—based on the detected weight values:
- **Normal**: 800kg ≤ weight ≤ 900kg
- **Overweight**: weight > 900kg
- **Underweight**: weight < 800kg

The real-time data is displayed on a user-friendly dashboard and securely stored in Firestore for historical tracking and further decision-making. The system is designed for scalability, allowing easy integration of additional sensors and monitoring features. It enhances operational efficiency by alerting stakeholders whenever a wagon is out of the predefined weight range, minimizing the risk of operational delays, maintenance issues, or regulatory non-compliance.

With robust security features and real-time analytics, this system provides an innovative solution for efficient freight management in rail transport.

# Setting Up the Virtual Environment to start application
Follow these steps to create and activate a virtual environment using **virtualenv**.

# 1. Change terminal to working directory
```bash
cd real-time-wagon-weigh-analysis
```
# 2. Install `virtualenv` (if not already installed)
First, ensure you have `virtualenv` installed globally on your system:
```bash
pip install virtualenv
```

# 3. Creating virtual environment
```bash
virtualenv env
.\env\Scripts\activate
```

# 4. Install Project Dependencies
```bash
pip install -r requirements.txt
```

# 5. Start running flask program
```bash
python app.py
```


