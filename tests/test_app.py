from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        text = response.data.decode('utf-8')
        assert "Сервер работает" in text

