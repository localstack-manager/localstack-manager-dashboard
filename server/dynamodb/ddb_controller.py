from flask import Blueprint, request, render_template

ddb_controller = Blueprint('ddb_controller', __name__, template_folder='templates')


@ddb_controller.route("/ddbList")
def ddb_list():
    return render_template('ddb/ddb-list.html')


@ddb_controller.route("/ddbItem")
def ddb_item():
    table_name = request.args.get('tableName')
    table_name = table_name if table_name else None
    return render_template('ddb/ddb-item.html', table_name=table_name)


@ddb_controller.route("/ddbListItems")
def ddb_list_items():
    table_name = request.args.get('tableName')
    table_name = table_name if table_name else None
    return render_template('ddb/ddb-list-items.html', table_name=table_name)
