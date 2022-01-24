from fastapi import FastAPI
from routers import root, health

app = FastAPI()
app.include_router(root.router)
app.include_router(health.router)
