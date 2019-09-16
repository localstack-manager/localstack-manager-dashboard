from flask import Flask, render_template

from server.dynamodb.ddb_controller import ddb_controller
from server.dynamodb.ddb_api import ddb_api

from server.s3.s3_controller import s3_controller
import server.s3.s3_service as s3
from server.s3.s3_api import s3_api

from server.sqs.sqs_controller import sqs_controller
from server.sqs.sqs_api import sqs_api

app = Flask(__name__)

app.register_blueprint(ddb_controller)
app.register_blueprint(ddb_api)

app.register_blueprint(s3_controller)
app.register_blueprint(s3_api)

app.register_blueprint(sqs_controller)
app.register_blueprint(sqs_api)

app.config['UPLOAD_FOLDER'] = s3.get_upload_folder_path()
app.secret_key = "super secret key"


@app.route("/")
def hello():    
    return render_template('index.html')
