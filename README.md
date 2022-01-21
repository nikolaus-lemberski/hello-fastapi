# Hello FastAPI

Hello World with Python and FastAPI 

## Start commands

... development
`uvicorn main:app --reload`

... production
`gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080`