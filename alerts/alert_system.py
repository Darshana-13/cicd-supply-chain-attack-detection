import json
from datetime import datetime
alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ALERT_FILE = "alerts.json"
alerts = []
def load_alerts():
    try:
        with open(ALERT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_alerts(alerts):
    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f)

alerts = load_alerts()

def send_alert(message):

    alert = {
        "message": message,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    alerts.append(alert)
    save_alerts(alerts)
    print(f"[{alert['time']}] {alert['message']}")

def get_alerts():
    return alerts

