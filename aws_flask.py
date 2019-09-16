import os
from flask import Flask, Blueprint, make_response, flash, request, redirect, url_for,  request, render_template
from flask.json import jsonify
from werkzeug.utils import secure_filename

import server.controller.sqs_manager as sqs
import server.controller.s3_manager as s3
from server.controller.ddb_controller import ddb_controller

app = Flask(__name__)
app.register_blueprint(ddb_controller)


DEFAULT_QUEUE = 'dann-car-queue'
DEFAULT_BUCKET = 'my-bucket'

app.config['UPLOAD_FOLDER'] = s3.getUploadFolderPath()
app.secret_key = "super secret key"

@app.route("/")
def hello():    
    return render_template('index.html')

@app.route("/sqsList")
def sqs_list():    
    return render_template('sqs/sqs-list.html')
    
    
@app.route("/sqsMessages")
def sqs_message(): 
    queue_name = request.args.get('queueName')
    queue_name = queue_name if queue_name else DEFAULT_QUEUE
    return render_template('sqs/sqs-messages.html', queue_name = queue_name)


@app.route("/s3List")
def s3_list():    
    return render_template('s3/s3-list-buckets.html')


@app.route("/s3ListFiles", methods=['GET', 'POST'])
def s3_files():    
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else DEFAULT_BUCKET
        
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("Uploading file: " + str(filename) + " to bucket:" + bucket_name)
            s3.upload_file(bucket_name, filename)
        return render_template('s3/s3-list-files.html', bucket_name = bucket_name)
    else:
        
        return render_template('s3/s3-list-files.html', bucket_name = bucket_name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
    
## --- REST SERVICES ---

@app.route("/api/s3AddBucket")
def add_s3_bucket():
    print("====================================================")
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else DEFAULT_BUCKET
    print('add bucket_name:{}'.format(bucket_name))
    
    s3.add_bucket(bucket_name)
    return jsonify("{'bucket added' : '"+bucket_name+"'}")
    
    
@app.route("/api/s3ListBuckets")
def list_s3_buckets():
    print("====================================================")
    buckets = s3.list_buckets()    
    return jsonify(buckets)

@app.route("/api/s3ListFiles")
def list_s3_files():
    print("====================================================")
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else DEFAULT_BUCKET
    print('bucket_name:{}'.format(bucket_name))
    
    files = s3.list_files(bucket_name)
    print('num messages in queue: {}'.format(files))
    return jsonify(files)
    
@app.route("/api/sqsListMessages")
def list_sqs_list_messages():
    print("====================================================")
    queue_name = request.args.get('queueName')
    queue_name = queue_name if queue_name else DEFAULT_QUEUE
    print('queue_name:{}'.format(queue_name))
    
    messages = sqs.list_messages(queue_name)
    print('num messages in queue: {}'.format(messages))
    return jsonify(messages)

@app.route("/api/sqsListQueues")
def list_sqs_queues():
    print("====================================================")
    queues_list = sqs.list_queues()
    return jsonify(queues_list)

@app.route("/api/sqsAddQueue")
def add_sqs_queue():
    print("====================================================")
    queue_name = request.args.get('queueName')
    if not queue_name:
        return 'queue name not informed'

    print('add queue_name:{}'.format(queue_name))    
    sqs.add_queue(queue_name)
    return jsonify("{'queue added' : '"+queue_name+"'}")
    
@app.route("/api/sqsAddMessageToQueue")
def add_sqs_message():
    print("====================================================")
    queue_name = request.args.get('queueName')
    message = request.args.get('message')

    if not queue_name:
        return 'queue name not informed'
    if not message:
        return 'message not informed'

    print('add message:{}'.format(message))    
    sqs.add_message_to_queue(message, queue_name)
    return jsonify("{'message added to queue' : '"+queue_name+"'}")