from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/app/health/readiness")
def readiness():
    return {"status": "ready"}


@app.get("/app/health/liveness")
def liveness():
    return {"status": "live"}