# load_gems

Нагрузочное тестирование API на базе [Locust](https://locust.io/).

## Структура

```
clients/                      # HTTP-клиенты по доменам
  guests/                     #   — гости
  loyalty/                    #   — программа лояльности
  discount_reasons/           #   — причины скидок
core/                         # Общие компоненты всех сценариев
  base_user.py                #   BaseUser: авторизация, host, wait_time
  task_sets.py                #   BaselineScenarioTaskSet: набор задач с весами
  load_shapes.py              #   StepLoadShape: ступенчатая нагрузка
  settings.py                 #   Настройки из .env (pydantic-settings)
  data.py                     #   Тестовые данные (hotel/guest/discount IDs)
scenarios/
  baseline/                   # Сценарий с постоянным числом пользователей
    baseline_scenario.py
    ide.conf                  #   Локальный прогон (15 мин, 50 users)
    workflow.conf             #   Smoke-прогон для CI (20 сек, 30 users)
  baseline_stepload/          # Сценарий со ступенчатым наращиванием нагрузки
    baseline_stepload_scenario.py
    ide.conf                  #   Локальный прогон (25→125 users за 15 мин)
reports/                      # Генерируемые HTML- и CSV-отчёты (не в VCS)
.github/workflows/
  load-test.yml               # GitHub Actions: запуск + публикация на Pages
```

## Быстрый старт

```bash
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env   # вставьте AUTH_TOKEN и BASE_URL
```

## Запуск

### Через флаг `-f` (указание locustfile напрямую)

```bash
# Локально с веб-интерфейсом (http://localhost:8089) — параметры задаются в UI
locust -f scenarios/baseline/baseline_scenario.py
```

### Через `--config` (файл конфигурации)

Файлы `.conf` позволяют зафиксировать параметры прогона рядом со сценарием.

```bash
# Локальный прогон baseline (15 мин, 50 пользователей)
locust --config scenarios/baseline/ide.conf

# Smoke-прогон для CI (20 сек, 30 пользователей)
locust --config scenarios/baseline/workflow.conf

# Ступенчатая нагрузка baseline_stepload (25→125 users за 15 мин)
locust --config scenarios/baseline_stepload/ide.conf
```

Пример содержимого `scenarios/baseline/ide.conf`:

```ini
locustfile = ./scenarios/baseline/baseline_scenario.py
users = 50
spawn-rate = 5
run-time = 15m
headless = false
html = ./reports/baseline/html_report.html
csv = baseline_scenario
csv-full-history = true
```

> Параметры из `--config` можно точечно переопределить прямо в командной строке:
> ```bash
> locust --config scenarios/baseline/ide.conf --users 100 --run-time 5m
> ```

## Переменные окружения (`.env`)

| Переменная  | Описание                      | Обязательная |
|-------------|-------------------------------|:----------:|
| `AUTH_TOKEN`| Bearer-токен для авторизации  |      ✅     |
| `BASE_URL`  | URL целевого сервиса          |     ✅      |

## CI / GitHub Actions

Запускается вручную через `workflow_dispatch`.  
После теста HTML-отчёт публикуется на **GitHub Pages** и архивируется как artifact.
