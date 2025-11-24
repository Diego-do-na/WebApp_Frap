def test_get_reportes(client):
    res = client.get("/reportes/")
    assert res.status_code == 200

def test_get_reporte_por_id(client):
    res = client.get("/reportes/1")
    assert res.status_code in (200, 404)

def test_get_reporte_completo(client):
    res = client.get("/reportes/completo/1")
    assert res.status_code in (200, 404)

def test_get_estadisticas(client):
    res = client.get("/reportes/estadisticas")
    assert res.status_code == 200