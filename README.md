# demo-py

Simple python Flask app that servers "hello world" 
Great for testing simple deployments to the cloud

## Build with poetry

Please be sure to have Python >3.9

```bash
pip install poetry
poetry install
poetry build
```

## Run with poetry

```bash
poetry run flask --app demo_py/app.py run
```

## Build with docker
```bash
docker build -t python-hello:1.0.0 .
```

## Run with docker
```bash
docker run -p 5000:5000 -e VERSION=1.0.0 python-hello:1.0.0
```
 
