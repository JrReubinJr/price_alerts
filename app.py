__author__ = 'Sincliar Solutions'

from flask import Flask
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = 'poop'

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(alert_blueprint, url_prefix="/stores")
app.register_blueprint(alert_blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(port=4995, debug=True)