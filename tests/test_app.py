import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_home():
    # Используем тестовый клиент Flask
    with app.test_client() as client:
        response = client.get('/')
        # Проверяем, что сервер ответил успешно
        assert response.status_code == 200
        # Проверяем, что есть текст "Сервер работает"
        assert b"Сервер работает" in response.data

