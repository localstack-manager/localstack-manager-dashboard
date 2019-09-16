var BASE_API_URL = 'http://localhost:5000/api/';

function list_buckets() {
	var tableBodySelector = $("#s3ListBucketsTableId tbody");
	tableBodySelector.empty();
	
    var url = BASE_API_URL + 's3ListBuckets'; //TODO add 'api'
    $.getJSON(url, function (data) {
        if (data && data.length > 0)
            for (index in data) {
                message = data[index];
                rowContent = '<tr>'
                    + '<td><a href="/s3ListFiles?bucketName='+message+'">' + message + '</a></td>'
                    + '<td><a href="#">Delete</a></td>'
                    + '</tr>';
                $("#s3ListBucketsTableId tbody").append(rowContent);
            }

        console.log(data);
    }, function (err) {
        console.log('Error:', err);
    });
}

function list_files(bucketName) {
	var tableBodySelector = $("#s3ListFilesTableId tbody");
    var bucketName = $('#bucketNameId').val();
    
    tableBodySelector.empty();
    var url = BASE_API_URL + 's3ListFiles?bucketName=' + bucketName;	
    $.getJSON(url, function (data) {
        if (data && data.length > 0)
			data = JSON.parse(data)
            for (index in data) {
                message = data[index];
                rowContent = '<tr>'
                + '<td>' + message.key + '</td>'
				+ '<td>' + message.size + ' bytes</td>'
                + '<td>' + message.last_modified + '</td>'
				+ '<td>' + message.owner + '</td>'
                + '<td><a href="#">Delete</a></td>'
                +'</tr>';
                tableBodySelector.append(rowContent);
            }

        console.log(data);
    }, function (err) {
        console.log('Error:', err);
    });
}

function addBucket() {
    var bucketName = $('#bucketNameId').val();
	console.log("add bucket: ", bucketName);
	var url = BASE_API_URL + 's3AddBucket?bucketName=' + bucketName;

    $.getJSON(url, function (data) {
        console.log("bucket added: ", bucketName);
		list_buckets();
    }, function (err) {
        console.log('Error:', err);
    });
}

