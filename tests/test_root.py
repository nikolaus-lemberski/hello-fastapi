from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert json.loads(res.content) == {"message": "Hello World"}
