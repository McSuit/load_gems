"""Базовый сценарий нагрузки с постоянным количеством пользователей."""
from core.base_user import BaseUser
from core.task_sets import BaselineScenarioTaskSet


class BaselineScenarioUser(BaseUser):
    """Locust-пользователь для базового сценария."""
    tasks = [BaselineScenarioTaskSet]