# demo-py

Simple python Flask app that servers "hello world" 
Great for testing simple deployments to the cloud


## Build 
`docker build -t python-hello:1.0.0 .`

## Run with docker
`docker run -p 5000:5000 -e VERSION=1.0.0 python-hello:1.0.0`

 
