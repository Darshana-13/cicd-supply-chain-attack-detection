from flask import Flask, render_template
from alerts.alert_system import get_alerts, send_alert
from feature_extractor.commit_features import extract_commit_features
from ml_model.detect_attack import predict_attack
from detectors.npm_dependency_checker import check_npm_dependencies

app = Flask(__name__)

def run_scan():
    features = extract_commit_features()
    if predict_attack(features) == "attack":
        send_alert("ML detected suspicious commit")
    suspicious_packages = check_npm_dependencies()
    if suspicious_packages:
        send_alert(f"Suspicious npm packages detected: {suspicious_packages}")

@app.route("/")
def dashboard():
    # Run scan in the same process
    run_scan()
    alerts = get_alerts()
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
