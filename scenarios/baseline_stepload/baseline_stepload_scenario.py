"""Сценарий нагрузки с ступенчатым наращиванием пользователей (StepLoadShape)."""
from core.base_user import BaseUser
from core.task_sets import BaselineScenarioTaskSet
from core.load_shapes import StepLoadShape


class BaselineStepLoadShape(StepLoadShape):
    """Форма ступенчатой нагрузки для этого сценария (наследует StepLoadShape)."""


class BaselineScenarioUser(BaseUser):
    """Locust-пользователь для базового ступенчатого сценария (используется с StepLoadShape)."""
    tasks = [BaselineScenarioTaskSet]
