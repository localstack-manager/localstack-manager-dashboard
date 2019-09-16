import boto3
import json
    
sqs = boto3.resource('sqs', endpoint_url="http://localhost:4576")
queue = sqs.get_queue_by_name(QueueName='dan-queue')

def receive_message():
    messages = queue.receive_messages(MaxNumberOfMessages=2, WaitTimeSeconds=5)
    return messages[0] if messages else None
    
    
while True:
    message = receive_message()
    if message:
        #body = json.loads(message.body)
        print('message: {}'.format(message.body))
        message.delete()
    else:
        print('No message received, exiting')
        break    
    



'''
s3 = boto3.client('s3', endpoint_url="http://localhost:4572")
print ('-- buckets-- ')
for obj in s3.list_buckets().get('Buckets'):
    print(obj.get('Name'))
print(s3.list_buckets())
'''
