"""HTTP-клиент для работы с API настроек лояльности."""
from locust import clients
from clients.loyalty.schema import GetLoyaltySettingsResponseSchema


class LoyaltyClient:
    """Обёртка над эндпоинтами API лояльности."""

    def __init__(self, client: clients.HttpSession):
        self.client = client

    def get_loyalty_settings(self, hotel_id: int) -> GetLoyaltySettingsResponseSchema | None:
        """Получить уровни и настройки лояльности для отеля."""
        with self.client.get(f"/api/v1/hotel/{hotel_id}/loyalty/settings",
                             name="/api/v1/hotel/{hotel_id}/loyalty/settings",
                             catch_response=True) as response:
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if "error" in response_json:
                        response.failure(f"Response contains 'error' key: {response_json['error']}")
                        return

                    validated_model = GetLoyaltySettingsResponseSchema.model_validate(response_json)
                    response.success()
                    return validated_model
                except Exception as e:
                    response.failure(f"Validation failed: {e}")
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")