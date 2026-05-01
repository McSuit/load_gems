"""HTTP-клиент для работы с API причин скидок."""
from clients.base_client import BaseClient
from clients.discount_reasons.schema import GetDiscountReasonResponse


class DiscountReasonsClient(BaseClient):
    """Обёртка над эндпоинтами API причин скидок."""

    def get_discount_reason(self, hotel_id: int,
                            discount_id: int) -> GetDiscountReasonResponse | None:
        """
        Получить причину скидки по ID отеля и ID причины.

        :param hotel_id: Идентификатор отеля.
        :param discount_id: Идентификатор причины скидки.
        :return: Ответ с причиной скидки или None в случае ошибки.
        """
        with self.client.get(f"/api/v1/hotel/{hotel_id}/discountReason/{discount_id}",
                             name="/api/v1/hotel/{hotel_id}/discountReason/{discount_id}",
                             catch_response=True) as response:
            return self._handle_response(response, GetDiscountReasonResponse)
