from fastapi import APIRouter

router = APIRouter()


@router.get("/app/health/readiness")
async def readiness():
    return {"status": "UP"}


@router.get("/app/health/liveness")
async def liveness():
    return {"status": "UP"}
