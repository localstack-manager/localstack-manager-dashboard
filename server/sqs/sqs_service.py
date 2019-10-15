import boto3

SQS_ENDPOINT = 'http://localhost:4576'
DEFAULT_QUEUE_NAME = 'default-queue'


def create_sqs_resource():
    return boto3.resource('sqs', endpoint_url=SQS_ENDPOINT, region_name='us-west-2')


def create_sqs_client():
    return boto3.client('sqs', endpoint_url=SQS_ENDPOINT, region_name='us-west-2')


def list_messages(queue_name):
    sqs = create_sqs_resource()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    message_list = []

    while True:
        message = receive_message(queue)
        if message:
            print('message: {}'.format(message.body))
            message_with_id = {'id': message.message_id, 'body': message.body}
            message_list.append(message_with_id)

        else:
            # print('No message received, exiting')
            break

    if len(message_list) == 0:
        message_list.append({'id': '-', 'body': 'no message received'})

    return message_list


def receive_message(queue):
    messages = queue.receive_messages(MaxNumberOfMessages=10, WaitTimeSeconds=2)
    return messages[0] if messages else None


def list_queues():
    sqs = create_sqs_resource()
    queue_list = sqs.queues.all()
    return [queue.url for queue in queue_list]


def add_queue(queue_name):
    sqs = create_sqs_resource()
    queue = sqs.create_queue(QueueName=queue_name)


def delete_queue(queue_url):
    sqs = create_sqs_client()
    sqs.delete_queue(QueueUrl=queue_url)


def add_message_to_queue(message, queue_name):
    sqs = create_sqs_resource()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    response = queue.send_message(MessageBody=message)
    return response.get('MessageId')


if __name__ == '__main__':
    # messages = list_messages('dann-car-queue')
    # print('num messages in queue: {}'.format(messages))
    for q in list_queues():
        print(q)
