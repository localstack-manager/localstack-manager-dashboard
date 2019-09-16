from flask import Blueprint, request
from flask.json import jsonify

import server.sqs.sqs_service as sqs_service

sqs_api = Blueprint('sqs_api', __name__, template_folder='templates')


@sqs_api.route("/api/sqsListMessages")
def list_sqs_list_messages():
    print("====================================================")
    queue_name = request.args.get('queueName')
    queue_name = queue_name if queue_name else sqs_service.DEFAULT_QUEUE_NAME
    print('queue_name:{}'.format(queue_name))

    messages = sqs_service.list_messages(queue_name)
    print('num messages in queue: {}'.format(messages))
    return jsonify(messages)


@sqs_api.route("/api/sqsListQueues")
def list_sqs_queues():
    print("====================================================")
    queues_list = sqs_service.list_queues()
    return jsonify(queues_list)


@sqs_api.route("/api/sqsAddQueue")
def add_sqs_queue():
    print("====================================================")
    queue_name = request.args.get('queueName')
    if not queue_name:
        return 'queue name not informed'

    print('add queue_name:{}'.format(queue_name))
    sqs_service.add_queue(queue_name)
    return jsonify("{'queue added' : '" + queue_name + "'}")


@sqs_api.route("/api/sqsAddMessageToQueue")
def add_sqs_message():
    print("====================================================")
    queue_name = request.args.get('queueName')
    message = request.args.get('message')

    if not queue_name:
        return 'queue name not informed'
    if not message:
        return 'message not informed'

    print('add message:{}'.format(message))
    sqs_service.add_message_to_queue(message, queue_name)
    return jsonify("{'message added to queue' : '" + queue_name + "'}")
