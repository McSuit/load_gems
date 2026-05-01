"""Базовый HTTP-клиент с общей логикой обработки ответов."""
from locust import clients


class BaseClient:
    """Базовый класс для всех HTTP-клиентов с поддержкой валидации ответов."""

    def __init__(self, client: clients.HttpSession):
        """
        Инициализация базового клиента.

        :param client: Сессия Locust для выполнения HTTP-запросов.
        """
        self.client = client

    def _handle_response(self, response, schema_class):
        """
        Проверить статус ответа, распарсить JSON и провалидировать Pydantic-моделью.

        :param response: Ответ от Locust.
        :param schema_class: Pydantic-модель для валидации ответа.
        :return: Провалидированный объект модели или None в случае ошибки.
        """
        if response.status_code != 200:
            response.failure(f"Status code {response.status_code}: {response.text}")
            return None

        try:
            response_json = response.json()
            if "error" in response_json:
                response.failure(f"Response contains 'error' key: {response_json['error']}")
                return None

            validated_model = schema_class.model_validate(response_json)
            response.success()
            return validated_model
        except Exception as e:
            response.failure(f"Validation failed: {e}")
            return None
