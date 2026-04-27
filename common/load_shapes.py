"""Кастомные формы нагрузки для Locust."""
from locust import LoadTestShape


class StepLoadShape(LoadTestShape):
    """Ступенчатая нагрузка: старт с 25 пользователей, +25 каждые 3 минуты, остановка после max_steps."""

    step_time = 180      # секунд на один шаг
    users_per_step = 25  # пользователей добавляется на каждом шаге
    spawn_rate = 5       # пользователей в секунду при спавне
    max_steps = 5        # тест останавливается на шаге 5 (итого 15 минут)

    def tick(self):
        """Возвращает (кол-во пользователей, spawn_rate) для текущего шага или None для остановки."""
        current_step = int(self.get_run_time()) // self.step_time

        if current_step >= self.max_steps:
            return None

        return (current_step + 1) * self.users_per_step, self.spawn_rate
