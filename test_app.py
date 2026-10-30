from app import app
from utils import calculate_total, average


def test_user_endpoint():
    assert app.test_client().get("/user?username=test").status_code == 200


def test_sql_injection_is_data():
    r = app.test_client().get("/user", query_string={"username": "' OR '1'='1"})
    assert r.get_data(as_text=True) == "[]"


def test_total():
    assert calculate_total([10, 20], 0.1) == 33.0


def test_average_empty():
    assert average([]) == 0
