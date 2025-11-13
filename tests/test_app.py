from app import app

def test_home():
    # Используем тестовый клиент Flask
    with app.test_client() as client:
        response = client.get('/')
        # Проверяем, что сервер ответил успешно
        assert response.status_code == 200
        # Проверяем, что есть текст "Сервер работает"
        assert b"Сервер работает" in response.data
