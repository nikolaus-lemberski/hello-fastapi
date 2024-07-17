# Hello FastAPI

Hello World with Python and FastAPI

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start commands

... tests

`pytest`

... development

`uvicorn main:app --reload`

... production

`gunicorn main:app`

## OpenShift deploy

### Deploy the app

`oc new-app https://github.com/nikolaus-lemberski/hello-fastapi.git --name=hello-fastapi --strategy=source`

### Set health probes

`oc set probe deployment hello-fastapi --readiness --get-url=http://:8080/app/health/readiness --initial-delay-seconds=10 --period=5`
`oc set probe deployment hello-fastapi --liveness --get-url=http://:8080/app/health/liveness --initial-delay-seconds=10 --period=5`




