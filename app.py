__author__ = 'Sincliar Solutions'

from flask import Flask, render_template, request
from models.item import Item
import json

app = Flask(__name__)
newItem = 'new_item.html'

@app.route('/', methods=['GET','POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_mongo()
    return render_template(newItem)

if __name__ == '__main__':
    app.run(port=4995, debug=True)