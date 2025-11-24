def test_get_insumos(client):
    res = client.get("/insumos/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_medicamentos(client):
    res = client.get("/insumos/medicamentos")
    assert res.status_code == 200

def test_get_insumo_por_id(client):
    res = client.get("/insumos/1")
    assert res.status_code in (200, 404)