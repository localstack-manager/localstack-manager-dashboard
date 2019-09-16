from flask import Blueprint, request, render_template
import server.sqs.sqs_service as sqs_service

sqs_controller = Blueprint('sqs_controller', __name__, template_folder='templates')


@sqs_controller.route("/sqsList")
def sqs_list():
    return render_template('sqs/sqs-list.html')


@sqs_controller.route("/sqsMessages")
def sqs_message():
    queue_name = request.args.get('queueName')
    queue_name = queue_name if queue_name else sqs_service.DEFAULT_QUEUE_NAME
    return render_template('sqs/sqs-messages.html', queue_name=queue_name)
