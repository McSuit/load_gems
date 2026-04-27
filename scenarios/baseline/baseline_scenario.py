import random
from locust import TaskSet, task
from common.base_user import BaseUser
from clients.guests.client import GuestsClient
from clients.loyalty.client import LoyaltyClient
from clients.discount_reasons.client import DiscountReasonsClient
from clients.guests.schema import CreateGuestRequestSchema
from data.data import (
    HOTEL_IDS,
    DISCOUNT_ID_RANGES,
    GUEST_ID_RANGES,
    CREATE_GUEST_HOTEL_ID
)


class BaselineScenarioTaskSet(TaskSet):
    """Набор задач, отражающий реальное соотношение запросов к API."""

    guests: GuestsClient
    loyalty: LoyaltyClient
    discount_reasons: DiscountReasonsClient

    def on_start(self):
        """
        Инициализация клиентов при старте каждого пользователя.
        Использование on_start — стандартный и безопасный способ в Locust.
        """
        self.guests = GuestsClient(self.client)
        self.loyalty = LoyaltyClient(self.client)
        self.discount_reasons = DiscountReasonsClient(self.client)

    @task(55)
    def get_guests(self):
        hotel_id = random.choice(HOTEL_IDS)
        self.guests.get_guests(hotel_id=hotel_id)

    @task(16)
    def get_loyalty_settings(self):
        hotel_id = random.choice(HOTEL_IDS)
        self.loyalty.get_loyalty_settings(hotel_id=hotel_id)

    @task(12)
    def get_discount_reason(self):
        hotel_id = random.choice(list(DISCOUNT_ID_RANGES.keys()))
        discount_id = random.randint(*DISCOUNT_ID_RANGES[hotel_id])
        self.discount_reasons.get_discount_reason(hotel_id=hotel_id, discount_id=discount_id)

    @task(9)
    def get_guest(self):
        hotel_id = random.choice(list(GUEST_ID_RANGES.keys()))
        guest_id = random.randint(*GUEST_ID_RANGES[hotel_id])
        self.guests.get_guest(hotel_id=hotel_id, guest_id=guest_id)

    @task(8)
    def create_guest(self):
        request = CreateGuestRequestSchema()
        self.guests.create_guest(request=request, hotel_id=CREATE_GUEST_HOTEL_ID)


class BaselineScenarioUser(BaseUser):
    """Locust-пользователь для базового сценария."""
    tasks = [BaselineScenarioTaskSet]
