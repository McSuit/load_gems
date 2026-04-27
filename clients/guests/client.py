"""HTTP-клиент для работы с API гостей."""
from locust import clients
from clients.guests.schema import (
    GetGuestsResponseSchema, GetGuestResponseSchema,
    CreateGuestRequestSchema, CreateGuestResponseSchema
)


class GuestsClient:
    """Обёртка над эндпоинтами API гостей."""

    def __init__(self, client: clients.HttpSession):
        self.client = client

    def get_guests(self, hotel_id: int) -> GetGuestsResponseSchema | None:
        """Получить постраничный список гостей отеля."""
        with self.client.get(f"/api/v1/hotel/{hotel_id}/guests",
                             name="/api/v1/hotel/{hotel_id}/guests",
                             catch_response=True) as response:
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if "error" in response_json:
                        response.failure(f"Response contains 'error' key: {response_json['error']}")
                        return

                    validated_model = GetGuestsResponseSchema.model_validate(response_json)
                    response.success()
                    return validated_model
                except Exception as e:
                    response.failure(f"Validation failed: {e}")
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")

    def get_guest(self, hotel_id: int, guest_id: int) -> GetGuestResponseSchema | None:
        """Получить одного гостя по ID."""
        with self.client.get(f"/api/v1/hotel/{hotel_id}/guests/{guest_id}",
                             name="/api/v1/hotel/{hotel_id}/guests/{guest_id}",
                             catch_response=True) as response:
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if "error" in response_json:
                        response.failure(f"Response contains 'error' key: {response_json['error']}")
                        return

                    validated_model = GetGuestResponseSchema.model_validate(response_json)
                    response.success()
                    return validated_model
                except Exception as e:
                    response.failure(f"Validation failed: {e}")
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")

    def create_guest(self, request: CreateGuestRequestSchema,
                      hotel_id: int) -> CreateGuestResponseSchema | None:
        """Создать нового гостя и вернуть его ID."""
        with self.client.post(f"/api/v1/hotel/{hotel_id}/guests",
                              json=request.model_dump(),
                              name="/api/v1/hotel/{hotel_id}/guests",
                              catch_response=True) as response:
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if "error" in response_json:
                        response.failure(f"Response contains 'error' key: {response_json['error']}")
                        return

                    validated_model = CreateGuestResponseSchema.model_validate(response_json)
                    response.success()
                    return validated_model
                except Exception as e:
                    response.failure(f"Validation failed: {e}")
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")
