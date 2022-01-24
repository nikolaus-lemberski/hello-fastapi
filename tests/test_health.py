from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)


def test_readiness():
    res = client.get("/app/health/readiness")
    assert res.status_code == 200
    assert json.loads(res.content) == {"status": "UP"}


def test_liveness():
    res = client.get("/app/health/liveness")
    assert res.status_code == 200
    assert json.loads(res.content) == {"status": "UP"}
