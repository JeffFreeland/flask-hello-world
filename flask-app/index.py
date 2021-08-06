from flask import Flask

import os
import urllib


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/env-var-1")
def env_var_1():
    DEFAULT_ENV_VAR = "ENV_VAR_1_NOT_SET"
    return os.getenv('ENV_VAR_1', default=DEFAULT_ENV_VAR)

@app.route("/env-var-2")
def env_var_2():
    DEFAULT_ENV_VAR = "ENV_VAR_2_NOT_SET"
    return os.getenv('ENV_VAR_2', default=DEFAULT_ENV_VAR)

# This returns only the first line of the file
@app.route("/from-file")
def from_file():
    DEFAULT_FILE_NAME = "config_file.txt"
    FILE_NAME = os.getenv('FILE_NAME', default=DEFAULT_FILE_NAME)
    with open(FILE_NAME, "r") as file:
        line = file.readline()
        return line
    return "Something went wrong"

@app.route("/from-other-service")
def from_other_service():
    SECOND_SERVICE_URL = os.getenv('SECOND_SERVICE_URL', default=None)
    if SECOND_SERVICE_URL == None: 
        return "There is no second service specified"
    
    try: 
        with urllib.request.urlopen(SECOND_SERVICE_URL) as response:
            return response.read()
    except: 
        return f"Something went wrong accessing the second service: {SECOND_SERVICE_URL}"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)