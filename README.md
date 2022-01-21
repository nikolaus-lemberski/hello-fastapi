# Hello FastAPI

Hello World with Python and FastAPI

## Start commands

... development

`uvicorn main:app --reload`

... production

`gunicorn main:app`

## OpenShift deploy

`oc new-app python:3.9-ubi8~https://github.com/nikolaus-lemberski/hello-fastapi.git --name=hello-fastapi --strategy=source`

`oc edit deployment hello-fastapi`

-> in containers section under "resources", add:
```yaml
        readinessProbe:
          initialDelaySeconds: 10
          timeoutSeconds: 2
          httpGet:
            path: /app/health/readiness
            port: 8080
        livenessProbe:
          initialDelaySeconds: 10
          periodSeconds: 2
          httpGet:
            path: /app/health/liveness
            port: 8080
```



