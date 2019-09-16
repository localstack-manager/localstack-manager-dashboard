from flask import Blueprint
from flask.json import jsonify

from server.dynamodb import ddb_service as ddb

ddb_api = Blueprint('ddb_api', __name__, template_folder='templates')
DEFAULT_BUCKET = 'my-bucket'


@ddb_api.route('/api/ddb/listTables')
def list_tables():
    list = ddb.list_tables()
    return jsonify(list)


@ddb_api.route('/api/ddb/listItems')
def list_items():
    list = ddb.list_all_table_items()
    return jsonify(list)
