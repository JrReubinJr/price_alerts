__author__ = 'Sincliar Solutions'

from flask import Blueprint, render_template, request, url_for, redirect
from models.store import Store
from models.user import requires_admin, requires_login
import json

store_blueprint = Blueprint('stores', __name__)

@store_blueprint.route('/')
@requires_login
def index():
    stores = Store.all()
    return render_template('stores/store_index.html', stores=stores)

@store_blueprint.route('/new', methods=['GET','POST'])
@requires_admin
def create_store():
    if request.method == 'POST':
        store_name = request.form['name']
        url_prefix = request.form['url_prefix']
        html_tag = request.form['tag']
        query = json.loads(request.form['query'])

        store = Store(store_name, url_prefix, html_tag, query)
        store.save_to_mongo()


    return render_template('stores/new_store.html')

@store_blueprint.route('/edit', methods=['GET', 'POST'])
@requires_admin
def edit_store(store_id):
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        store.name = request.form['name']
        store.url_prefix = request.form['url_prefix']
        store.tag_name = request.form['tag']
        store.query = json.loads(request.form['query'])

        store.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/edit_store.html', store=store)

@store_blueprint.route('/delete/<string:alert_id>')
def delete_store(store_id):
    Store.get_by_id(store_id).remove_from_monogo()
    return redirect(url_for('.index'))