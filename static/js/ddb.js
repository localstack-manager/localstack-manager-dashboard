var BASE_API_URL = 'http://localhost:5000/api/';

function list_tables() {
	var tableBodySelector = $("#ddbListTablesId tbody");
	tableBodySelector.empty();
	
    var url = BASE_API_URL + 'ddb/listTables';
    $.getJSON(url, function (data) {
        if (data && data.length > 0)
            for (index in data) {
                table = data[index];	
                rowContent = '<tr>'
                    + '<td><a href="/ddbListItems?tableName='+table.table_name+'">' + table.table_name + '</a></td>'
					+ '<td><a href="/ddbListItems?tableName='+table.item_count+'">' + table.item_count + '</a></td>'
					+ '<td><a href="/ddbListItems?tableName='+table.table_size_bytes+'">' + table.table_size_bytes + ' bytes</a></td>'
					+ '<td><a href="/ddbListItems?tableName='+table.table_status+'">' + table.table_status + '</a></td>'

                    + '<td><a href="#">Delete</a></td>'
                    + '</tr>';
                tableBodySelector.append(rowContent);
            }

    }, function (err) {
        console.log('Error:', err);
    });
}

function list_items() {
	var tableBodySelector = $("#ddbListItemsId tbody");
	var tableHeaderSelector = $("#ddbListItemsId thead");
	
    var tableName = $('#tableNameId').val();
    
    tableBodySelector.empty();
	tableHeaderSelector.empty();
    var url = BASE_API_URL + 'ddb/listItems?tableName=' + tableName;	
    $.getJSON(url, function (data) {
        if (data && data.length > 0)
			var headers = extractHeaders(data[0]);
			createHeaders(headers, tableHeaderSelector);
			
			for (index in data) {
                item = data[index];
                rowContent = '<tr>'
				for (header in headers) {
					var headerName = headers[header]; 
					var itemValue = item[headerName] ? item[headerName] : '';
					rowContent += '<td>' + itemValue + '</td>'		
				}
				rowContent += '<td><a href="#">View details</a></td>'	
                rowContent += '<td><a href="#">Delete</a></td>'			
                rowContent += '</tr>';
                tableBodySelector.append(rowContent);
            }

        console.log(data);
    }, function (err) {
        console.log('Error:', err);
    });
}

function extractHeaders(item){
	var headers = [];
	for (attribute in item) {
		headers.push(attribute)
	}
	headers.sort();
	
	var indexId = headers.indexOf('id');
	if(indexId >= 0){
		headers.splice(indexId, 1);
		headers.unshift('id');		
	}		
		
	return headers;
}

function createHeaders(headers, tableHeaderSelector){
	var headerBuilder = '<tr>';
	for (header in headers) {
		var headerName = headers[header]; 
		headerBuilder += '<td>' + headerName + '</td>'
	}
	headerBuilder += '<td></td>'; 	//details column
	headerBuilder += '<td></td>';	//delete column
	headerBuilder += '</tr>';
	tableHeaderSelector.append(headerBuilder);
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

