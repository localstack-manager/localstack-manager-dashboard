import os
import subprocess
import threading
import time

def start_docker_images():
    print("Starting docker-compose")
    subprocess.call("docker-compose down")
    subprocess.call("docker-compose up")
    
def execute_docker_compose():   
    print("Starting Images: Localstack - DynamoDB")
    x = threading.Thread(target=start_docker_images, args = ())
    x.start()
    
    print("Waiting for images finish starting ... ")
    time.sleep(25)

def open_venv():
    print("Opening venv")
    # TODO: find a way to open a venv through python script
    # for now, do the process manually
    # windows:  venv\Scripts\activate
    # linux:    source env/bin/activate
    
def start_localstack_manager():
    print("Starting Localstack Manager")
    os.environ["FLASK_APP"] = "aws_flask.py"
    os.environ["FLASK_ENV"] = "development"
    print(os.getcwd())
    subprocess.call("flask run")


if __name__ == '__main__':        
    #open_venv()
    execute_docker_compose()
    #start_localstack_manager()
    
    
