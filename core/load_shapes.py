"""Кастомные формы нагрузки для Locust."""
from locust import LoadTestShape


class StepLoadShape(LoadTestShape):
    """Базовая ступенчатая нагрузка. Определите параметры в подклассе."""

    step_time: int       # секунд на один шаг
    users_per_step: int  # пользователей добавляется на каждом шаге
    spawn_rate: int      # пользователей в секунду при спавне
    max_steps: int       # количество шагов до остановки теста

    def tick(self):
        """Возвращает (кол-во пользователей, spawn_rate) для текущего шага или None для остановки."""
        current_step = int(self.get_run_time()) // self.step_time

        if current_step >= self.max_steps:
            return None

        return (current_step + 1) * self.users_per_step, self.spawn_rate
