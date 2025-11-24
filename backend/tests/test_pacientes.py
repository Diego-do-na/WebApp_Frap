def test_obtener_pacientes(client):
    res = client.get("/pacientes/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_obtener_paciente_por_id(client):
    res = client.get("/pacientes/1")
    assert res.status_code in (200, 404)

def test_buscar_pacientes(client):
    res = client.get("/pacientes/buscar?nombre=Juan")
    assert res.status_code == 200