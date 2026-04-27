# load_gems

Нагрузочное тестирование API на базе [Locust](https://locust.io/).

## Структура

```
clients/          # HTTP-клиенты по доменам (guests, loyalty, discount_reasons)
common/           # BaseUser, StepLoadShape, Settings
data/             # Тестовые данные (hotel IDs, guests IDs, discount IDs)
scenarios/
  baseline/       # Сценарий + конфиги запуска
    ide.conf      # Полный прогон (15 мин, 50 users)
    workflow.conf # Smoke-прогон для CI (20 сек, 30 users)
.github/workflows/load-test.yml  # GitHub Actions: запуск + публикация HTML-отчёта на Pages
```

## Быстрый старт

```bash
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env   # вставьте AUTH_TOKEN и BASE_URL
```

## Запуск

```bash
# Локально с веб-интерфейсом (http://localhost:8089)
locust -f scenarios/baseline/baseline_scenario.py

# Headless, полный прогон (15 мин)
locust --config scenarios/baseline/ide.conf

# Headless, smoke (20 сек, используется в CI)
locust --config scenarios/baseline/workflow.conf
```

## Переменные окружения (`.env`)

| Переменная  | Описание                      | Обязательная |
|-------------|-------------------------------|:----------:|
| `AUTH_TOKEN`| Bearer-токен для авторизации  |      ✅     |
| `BASE_URL`  | URL целевого сервиса           |     ✅      |

## CI / GitHub Actions

Запускается вручную через `workflow_dispatch`.  
После теста HTML-отчёт публикуется на **GitHub Pages** и архивируется как artifact.
