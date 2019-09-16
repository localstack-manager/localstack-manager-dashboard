var BASE_API_URL = 'http://localhost:5000/api/';


function list_queues() {
	var tableBodySelector = $("#sqsListTableId tbody");
	tableBodySelector.empty();
	
    var url = BASE_API_URL + 'sqsListQueues';

    $.getJSON(url, function (data) {
        if (data && data.length > 0)
            for (index in data) {
                message = data[index];
                rowContent = '<tr>'
                    + '<td><a href="/sqsMessages?queueName='+extratQueueName(message)+'">' + message + '</a></td>'
                    + '<td><a href="#">Delete</a></td>'
                    + '</tr>';
                tableBodySelector.append(rowContent);
            }

        console.log(data);
    }, function (err) {
        console.log('Error:', err);
    });
}

function extratQueueName(message){
    queue_name = message.substring(message.lastIndexOf('/') + 1);
    return queue_name
}


function list_messages() {    
	var tableBodySelector = $("#sqsTableId tbody");
    tableBodySelector.empty();
	
    var queueName = $('#queueNameId').val();
    var url = BASE_API_URL + 'sqsListMessages?queueName=' + queueName;

    $.getJSON(url, function (data) {
        if (data && data.length > 0)
            for (index in data) {
                message = data[index];
                rowContent = '<tr>'
                + '<td>' + message.id + '</td>'
                + '<td>' + message.body + '</td>'
                + '<td><a href="#">Delete</a></td>'
                +'</tr>';
                tableBodySelector.append(rowContent);
            }

        console.log(data);
    }, function (err) {
        console.log('Error:', err);
    });
}

function poll_messages(){
	list_messages();
	window.setInterval(function () {
		list_messages();
	}, 8000);
}

function addMessage() {
    var message = $('#messageId').val();
	var queueName = $('#queueNameId').val();
	console.log("add message to queue: ", queueName, message);
    
    var url = BASE_API_URL + 'sqsAddMessageToQueue?queueName=' + queueName +'&message='+message;

    $.getJSON(url, function (data) {
        console.log("message added ");
		list_messages();
    }, function (err) {
        console.log('Error:', err);
    });
}

function addQueue() {
    var queueName = $('#queueNameId').val();
	console.log("add queue: ", queueName);
	var url = BASE_API_URL + 'sqsAddQueue?queueName=' + queueName;

    $.getJSON(url, function (data) {
        console.log("queue added: ", queueName);
		list_queues();
    }, function (err) {
        console.log('Error:', err);
    });
}