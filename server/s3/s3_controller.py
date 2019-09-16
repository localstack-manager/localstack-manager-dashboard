import os
from flask import Blueprint, flash, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

import server.s3.s3_service as s3_service

s3_controller = Blueprint('s3_controller', __name__, template_folder='templates')


@s3_controller.route("/s3List")
def s3_list():
    return render_template('s3/s3-list-buckets.html')


@s3_controller.route("/s3ListFiles", methods=['GET', 'POST'])
def s3_files():
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else s3_service.DEFAULT_BUCKET_NAME

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
            file.save(os.path.join(s3_service.get_upload_folder_path(), filename))
            print("Uploading file: " + str(filename) + " to bucket:" + bucket_name)
            s3_service.upload_file(bucket_name, filename)
        return render_template('s3/s3-list-files.html', bucket_name=bucket_name)
    else:

        return render_template('s3/s3-list-files.html', bucket_name=bucket_name)


@s3_controller.route('/upload', methods=['GET', 'POST'])
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
            file.save(os.path.join(s3_service.get_upload_folder_path(), filename))
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
