__author__ = 'Sincliar Solutions'

from flask import Flask
from views.alerts import alert_blueprint

app = Flask(__name__)

app.register_blueprint(alert_blueprint, url_prefix="/alerts")

if __name__ == '__main__':
    app.run(port=4995, debug=True)