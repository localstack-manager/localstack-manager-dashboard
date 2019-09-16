import boto3
import json


S3_ENDPOINT = 'http://localhost:4572'
UPLOAD_FOLDER = 'uploads'  # 'D:\\learn-py\\aws-lambdas\\uploads'
DEFAULT_BUCKET_NAME = 'bucket-name-default'


class S3Object:
    def __init__(self, key, size, last_modified, owner):
        self.key = key
        self.size = size
        self.last_modified = str(last_modified)
        self.owner = owner

    def __repr__(self):
        return 'key: {} - size: {}KB'.format(self.key, (self.size / 1000))


def create_s3_resource():
    return boto3.resource('s3', endpoint_url=S3_ENDPOINT, region_name='us-west-2')


def create_s3_client():
    return boto3.client('s3', endpoint_url=S3_ENDPOINT, region_name='us-west-2')


def list_buckets():
    s3 = create_s3_client()
    return [obj.get('Name') for obj in s3.list_buckets().get('Buckets')]


def list_files(bucket_name):
    s3 = create_s3_resource()
    bucket = s3.Bucket(bucket_name)
    bucket_files = []
    for s3_file in bucket.objects.all():
        s3_obj = S3Object(s3_file.key, s3_file.size, s3_file.last_modified, s3_file.owner.get('DisplayName'))
        bucket_files.append(s3_obj)
    return json.dumps([ob.__dict__ for ob in bucket_files])


def get_upload_folder_path():
    return UPLOAD_FOLDER


def upload_file(bucket_name, file_name):
    s3 = create_s3_resource()
    s3.Bucket(bucket_name).upload_file(get_upload_folder_path() + "/" + file_name, file_name)
    print("File: " + file_name + "uploaded.")


def add_bucket(bucket_name):
    s3 = create_s3_client()
    s3.create_bucket(Bucket=bucket_name)


if __name__ == '__main__':
    # print(list_buckets())
    print(list_files(list_buckets()[0]))
    list_files('my-bucket')
