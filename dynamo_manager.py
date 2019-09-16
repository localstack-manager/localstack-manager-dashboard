import boto3
import uuid
import json
import hashlib

DYNAMO_ENDPOINT = 'http://localhost:8000'


def create_resource():
    return boto3.resource('dynamodb', endpoint_url=DYNAMO_ENDPOINT, region_name='us-west-2')
    
def create_client():
    return boto3.client('dynamodb', endpoint_url=DYNAMO_ENDPOINT, region_name='us-west-2')

def list_all_table_items():
    dynamodb = create_resource()
    table = dynamodb.Table('file-import-process')
    response = table.scan()
    data = response['Items']
    print(data)
    return data






def list_tables():    
    response = create_client().list_tables()
    table_list_detail = []
    table_list = response.get('TableNames')
    for table_name in table_list:
        table_info = describe_table(table_name)
        table_detail = create_table_detail(table_info.get('Table'))
        table_list_detail.append(table_detail)
    return table_list_detail
    
def describe_table(table_name):
    table_detail = create_client().describe_table(TableName=table_name)
    return table_detail

def create_table_detail(table):
    table_detail = {
        'table_name' : table['TableName'],
        'item_count' : table['ItemCount'],
        'table_status' : table['TableStatus'],
        'table_size_bytes' : table['TableSizeBytes']
    }
    return table_detail
