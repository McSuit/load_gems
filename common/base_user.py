"""Базовый Locust-пользователь, общий для всех сценариев."""
from locust import HttpUser, between
from common.settings import settings


class BaseUser(HttpUser):
    """Абстрактный HTTP-пользователь. Добавляет Bearer-токен в заголовки при старте."""

    abstract = True
    host = settings.base_url
    wait_time = between(1, 5)

    def on_start(self):
        token = settings.auth_token.get_secret_value()
        self.client.headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}'
        })
