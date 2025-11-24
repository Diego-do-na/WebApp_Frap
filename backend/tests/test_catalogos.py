def test_get_alergias(client):
    res = client.get("/catalogos/alergias")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_patologias(client):
    res = client.get("/catalogos/patologias")
    assert res.status_code == 200

def test_get_pupilas(client):
    res = client.get("/catalogos/pupilas")
    assert res.status_code == 200

def test_get_nivel_conciencia(client):
    res = client.get("/catalogos/nivel_conciencia")
    assert res.status_code == 200

def test_get_anatomica(client):
    res = client.get("/catalogos/anatomica")
    assert res.status_code == 200

def test_get_lugares(client):
    res = client.get("/catalogos/lugares")
    assert res.status_code == 200

def test_get_signos_vitales(client):
    res = client.get("/catalogos/signos_vitales")
    assert res.status_code == 200