# flask-hello-world
A "hello world" app for flask

It runs on port 5000, and the root path `/` simply returns `"Hello World!"`

Paths and output: 

`/`         : `"Hello World!"`

`/env-var-1`: Value of `ENV_VAR_1`

`/env-var-2`: Value of `ENV_VAR_2`

`/from-file`: The first line of the file specified by `FILE_NAME`. The default file is located at `/app/config_file.txt`. 

`/from-other-service`: Returns the result of a get request to the url specified by `SECOND_SERVICE_URL`, where url is a fully qualified name including port if necessary. For example, `http://second-service-name:5000/env-var-1`. 