from flask import Flask, Blueprint, make_response, flash, request, redirect, url_for,  request, render_template
from flask.json import jsonify
import dynamo_manager as ddb

ddb_controller = Blueprint('ddb_controller', __name__, template_folder='templates')

@ddb_controller.route('/ddb/test')
def test():
    #result = ddb.list_tables()
    result = ddb.list_all_table_items()
    
    return jsonify(result)
    
@ddb_controller.route("/ddbList")
def ddb_list():
    return render_template('ddb/ddb-list.html')

@ddb_controller.route("/ddbItem")	
def ddb_item():
    table_name = request.args.get('tableName')
    table_name = table_name if table_name else None
    return render_template('ddb/ddb-item.html', table_name = table_name)

@ddb_controller.route("/ddbListItems")
def ddb_list_items():
    table_name = request.args.get('tableName')
    table_name = table_name if table_name else None
    return render_template('ddb/ddb-list-items.html', table_name = table_name)   
    
## --- REST SERVICES ---

@ddb_controller.route('/api/ddb/listTables')
def list_tables():
    list = ddb.list_tables()
    return jsonify(list)

@ddb_controller.route('/api/ddb/listItems')
def list_items():
    list = ddb.list_all_table_items()
    return jsonify(list)