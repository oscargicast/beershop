from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_order_success(order):
    response = client.get("/api/v1/orders/order-1")
    assert response.status_code == 200
    assert response.json().get("subtotal") == order.subtotal
    assert len(response.json().get("items")) == len(order.items)
    assert len(response.json().get("rounds")) == len(order.rounds)


def test_not_found_order():
    response = client.get("/api/v1/orders/invalid-order")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
    # A not instanciated order.
    response = client.get("/api/v1/orders/order-1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
