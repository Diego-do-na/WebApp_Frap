def test_registrar_usuario(client):
    payload = {
        "nombre": "Usuario Test",
        "email": "usertest@example.com",
        "password": "123456"
    }
    res = client.post("/usuarios/registrar", json=payload)
    assert res.status_code in (200, 400)

def test_login_usuario(client):
    payload = {
        "email": "usertest@example.com",
        "password": "123456"
    }
    res = client.post("/usuarios/login", json=payload)
    assert res.status_code in (200, 401)