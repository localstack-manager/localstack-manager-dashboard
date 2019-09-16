import boto3

DYNAMODB_ENDPOINT = 'http://localhost:8000'


class Car:
    def __init__(self, id, name, brand):
        self.id = id
        self.name = name
        self.brand = brand
    
    def __repr__(self):
        return 'id: {} name: {}({})'.format(self.id, self.name, self.brand)

class MessageItemResponse:
    def __init__(self, message_id, md5, body):
        self.message_id = message_id
        self.md5 = md5
        self.body = body
    
    def __repr__(self):
        return 'id: {} body: {}'.format(self.message_id, self.body)


if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMODB_ENDPOINT)

    table = dynamodb.Table('dann-table')
    print('name: {} status: {} count: {}'.format(table.table_name, table.table_status, table.item_count))
    
    car1 = Car('1', 'Fox', 'VW')
    car2 = Car('2', 'Gol', 'VW')
    car3 = Car('3', 'Civic', 'Honda')

    table.put_item(Item=car1.__dict__)
    table.put_item(Item=car2.__dict__)
    table.put_item(Item=car3.__dict__)
    
    response = table.get_item(TableName='dann-table', Key={'id': '34'})
    print(response['Item'])