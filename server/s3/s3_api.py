from flask import Blueprint, request
from flask.json import jsonify

import server.s3.s3_service as s3_service

s3_api = Blueprint('s3_api', __name__, template_folder='templates')
DEFAULT_BUCKET = 'my-bucket'


@s3_api.route("/api/s3AddBucket")
def add_s3_bucket():
    print("====================================================")
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else DEFAULT_BUCKET
    print('add bucket_name:{}'.format(bucket_name))

    s3_service.add_bucket(bucket_name)
    return jsonify("{'bucket added' : '" + bucket_name + "'}")


@s3_api.route("/api/s3DeleteBucket")
def delete_s3_bucket():
    print("====================================================")
    bucket_name = request.args.get('bucketName')
    if not bucket_name:
        return 'bucket_name not informed'
    print('delete bucket_name:{}'.format(bucket_name))

    s3_service.delete_bucket(bucket_name)
    return jsonify("{'bucket deleted' : '" + bucket_name + "'}")


@s3_api.route("/api/s3ListBuckets")
def list_s3_buckets():
    print("====================================================")
    buckets = s3_service.list_buckets()
    return jsonify(buckets)


@s3_api.route("/api/s3ListFiles")
def list_s3_files():
    print("====================================================")
    bucket_name = request.args.get('bucketName')
    bucket_name = bucket_name if bucket_name else DEFAULT_BUCKET
    print('bucket_name:{}'.format(bucket_name))

    files = s3_service.list_files(bucket_name)
    print('num messages in queue: {}'.format(files))
    return jsonify(files)
