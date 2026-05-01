"""Сценарий нагрузки с ступенчатым наращиванием пользователей (StepLoadShape)."""
from core.base_user import BaseUser
from core.task_sets import BaselineScenarioTaskSet
from core.load_shapes import StepLoadShape


class BaselineStepLoadShape(StepLoadShape):
    """Ступенчатая нагрузка для базового сценария."""

    step_time = 180        # секунд на один шаг
    users_per_step = 25    # пользователей добавляется на каждом шаге
    spawn_rate = 5         # пользователей в секунду при спавне
    max_steps = 5          # количество шагов до остановки теста


class BaselineScenarioUser(BaseUser):
    """Locust-пользователь для базового ступенчатого сценария (используется с StepLoadShape)."""
    tasks = [BaselineScenarioTaskSet]
