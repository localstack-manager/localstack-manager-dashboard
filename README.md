

# Localstack Manager

This project aims to help the developers when using Localstack to manage the AWS services that are running locally.


## Configuration

#### Install venv
```
pip install virtualenv
```

#### Create/Activate venv:
- Linux
```
python3 -m venv venv
source env/bin/activate
```

- Windows:
```
virtualenv env
venv\Scripts\activate
```

### Install dependencies
``` 
pip install -r requirements.txt
```

### Run Localstack using docker-compose

Open a terminal the the root directory of the repository, then execute the docker-compose up:

```
cd /home/localstack-manager
docker-compose up
```

## FLASK APP

- Linux
```
pip install Flask

export FLASK_APP=aws_flask.py
export FLASK_ENV=development
flask run
```

- Windows:
 ```
set FLASK_APP=aws_flask.py
set FLASK_ENV=development
flask run
```


### SQS Commands example
```
aws sqs create-queue --queue-name testqueue --endpoint-url=http://localhost:4576 
aws sqs send-message --queue-url http://localhost:4576/queue/testqueue  --endpoint-url=http://localhost:4576  --message-body 'Test Message!' 
aws sqs receive-message --queue-url http://localhost:4576/queue/testqueue --endpoint-url=http://localhost:4576
```
```
1. Car queue

aws sqs create-queue --queue-name dann-car-queue --endpoint-url=http://localhost:4576
aws sqs receive-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576
aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body '{"name" : "Fox", "brand" : "VW"}'

aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body "{\"name\" : \"Fox\", \"brand\" : \"VW\"}" 
aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body "body message 1" 

aws sqs purge-queue --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576

aws --endpoint-url=http://localhost:4576 sqs receive-message --queue-url http://localhost:4576/queue/user-created-event-queue


aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body '{"name" : "Uno", "brand" : "Fiat"}'
aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body '{"name" : "Palio", "brand" : "Fiat"}'
aws sqs send-message --queue-url http://localhost:4576/queue/dann-car-queue --endpoint-url=http://localhost:4576 --message-body '{"name" : "Siena", "brand" : "Fiat"}'

```

==================
### Lambda Commands example
```
aws lambda create-function --function-name=f1 --runtime=python3.6 --role=r1 --handler=lambda.handler --zip-file fileb://lambda.zip --endpoint-url=http://localhost:4574
aws lambda update-function-code --function-name=f1 --zip-file fileb://lambda.zip --endpoint-url=http://localhost:4574
aws lambda invoke --function-name f1 result.log --endpoint-url=http://localhost:4574


aws lambda create-function --function-name=f1 --runtime=python3.6 --role=r1 --handler=dynamo_lambda.handler --zip-file fileb://dynamo_lambda.zip --endpoint-url=http://localhost:4574 

aws lambda update-function-code --function-name=f1 --zip-file fileb://dynamo_lambda.zip --endpoint-url=http://localhost:4574 

aws lambda delete-function --function-name=f1 --endpoint-url=http://localhost:4574 

aws lambda invoke --function-name f1 result.log --endpoint-url=http://localhost:4574 

 
zip dynamo_lambda.zip dynamo_lambda.py|
```
### S3 Commands example
```
aws s3api create-bucket --bucket my-bucket --region us-west-2 --endpoint-url="http://localhost:4572"
aws s3 cp result.log s3://my-bucket --endpoint-url=http://localhost:4572
aws s3 cp s3_manager.py s3://my-bucket --endpoint-url=http://localhost:4572
aws s3 ls s3://my-bucket --endpoint-url=http://localhost:4572
```

### DynamoDB run without docker-compose
```
docker run -p 8000:8000 -it --rm instructure/dynamo-local-admin
```

### Usefull links

https://rmsol.de/2018/05/10/Localstack/

https://stackoverflow.com/questions/10180851/how-to-get-all-messages-in-amazon-sqs-queue-using-boto-library-in-python