"""HTTP-клиент для работы с API причин скидок."""
from locust import clients
from clients.discount_reasons.schema import GetDiscountReasonResponse


class DiscountReasonsClient:
    """Обёртка над эндпоинтами API причин скидок."""

    def __init__(self, client: clients.HttpSession):
        self.client = client

    def get_discount_reason(self, hotel_id: int,
                            discount_id: int) -> GetDiscountReasonResponse | None:
        """Получить причину скидки по ID отеля и ID причины."""
        with self.client.get(f"/api/v1/hotel/{hotel_id}/discountReason/{discount_id}",
                             name="/api/v1/hotel/{hotel_id}/discountReason/{discount_id}",
                             catch_response=True) as response:
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    if "error" in response_json:
                        response.failure(f"Response contains 'error' key: {response_json['error']}")
                        return

                    validated_model = GetDiscountReasonResponse.model_validate(response_json)
                    response.success()
                    return validated_model
                except Exception as e:
                    response.failure(f"Validation failed: {e}")
            else:
                response.failure(f"Status code {response.status_code}: {response.text}")
