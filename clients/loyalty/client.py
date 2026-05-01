"""HTTP-клиент для работы с API настроек лояльности."""
from clients.base_client import BaseClient
from clients.loyalty.schema import GetLoyaltySettingsResponseSchema


class LoyaltyClient(BaseClient):
    """Обёртка над эндпоинтами API лояльности."""

    def get_loyalty_settings(self, hotel_id: int) -> GetLoyaltySettingsResponseSchema | None:
        """
        Получить уровни и настройки лояльности для отеля.

        :param hotel_id: Идентификатор отеля.
        :return: Настройки лояльности или None в случае ошибки.
        """
        with self.client.get(f"/api/v1/hotel/{hotel_id}/loyalty/settings",
                             name="/api/v1/hotel/{hotel_id}/loyalty/settings",
                             catch_response=True) as response:
            return self._handle_response(response, GetLoyaltySettingsResponseSchema)
