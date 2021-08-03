from flask import Flask

import os


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)