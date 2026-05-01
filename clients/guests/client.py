"""HTTP-клиент для работы с API гостей."""
from clients.base_client import BaseClient
from clients.guests.schema import (
    GetGuestsResponseSchema, GetGuestResponseSchema,
    CreateGuestRequestSchema, CreateGuestResponseSchema
)


class GuestsClient(BaseClient):
    """Обёртка над эндпоинтами API гостей."""

    def get_guests(self, hotel_id: int) -> GetGuestsResponseSchema | None:
        """
        Получить постраничный список гостей отеля.

        :param hotel_id: Идентификатор отеля.
        :return: Список гостей или None в случае ошибки.
        """
        with self.client.get(f"/api/v1/hotel/{hotel_id}/guests",
                             name="/api/v1/hotel/{hotel_id}/guests",
                             catch_response=True) as response:
            return self._handle_response(response, GetGuestsResponseSchema)

    def get_guest(self, hotel_id: int, guest_id: int) -> GetGuestResponseSchema | None:
        """
        Получить одного гостя по ID.

        :param hotel_id: Идентификатор отеля.
        :param guest_id: Идентификатор гостя.
        :return: Данные гостя или None в случае ошибки.
        """
        with self.client.get(f"/api/v1/hotel/{hotel_id}/guests/{guest_id}",
                             name="/api/v1/hotel/{hotel_id}/guests/{guest_id}",
                             catch_response=True) as response:
            return self._handle_response(response, GetGuestResponseSchema)

    def create_guest(self, request: CreateGuestRequestSchema,
                      hotel_id: int) -> CreateGuestResponseSchema | None:
        """
        Создать нового гостя.

        :param request: Данные для создания гостя.
        :param hotel_id: Идентификатор отеля.
        :return: Ответ с ID созданного гостя или None в случае ошибки.
        """
        with self.client.post(f"/api/v1/hotel/{hotel_id}/guests",
                              json=request.model_dump(),
                              name="/api/v1/hotel/{hotel_id}/guests",
                              catch_response=True) as response:
            return self._handle_response(response, CreateGuestResponseSchema)
