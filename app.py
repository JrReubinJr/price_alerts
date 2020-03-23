__author__ = 'Sincliar Solutions'

import os
from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from libs.mailgun import Mailgun

app = Flask(__name__)
app.secret_key = 'poop'
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(alert_blueprint, url_prefix="/stores")
app.register_blueprint(alert_blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(port=4995, debug=True)