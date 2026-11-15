# MLOps basic — ДЗ №3

Простой воспроизводимый пайплайн с DVC:

1. `generate` создаёт CSV со 100 случайными целыми числами от 0 до 100, seed — 42.
2. `summarize` сохраняет количество, среднее, минимум и максимум в JSON.

## Запуск

Требуются Python 3.12 и UV. Из корня проекта:

```bash
uv sync --frozen
uv run dvc repro
uv run dvc metrics show
uv run dvc dag
uv run dvc push
uv run dvc status
```

Повторный `dvc repro` пропускает стадии, если код и данные не изменились.

## Хранение данных

Remote `storage` настроен на локальную папку `.dvc-storage/`.
CSV хранится в DVC, а код, конфигурация, `dvc.lock` и метрики — в Git.
Исходные числа воспроизводятся генератором, скачивать датасет не требуется.

Для восстановления данных из remote: `uv run dvc pull`.
После клонирования Git содержимое локального remote нужно перенести отдельно
или указать путь к доступному хранилищу:

```bash
uv run dvc remote modify --local storage url /path/to/storage
uv run dvc pull
```

Без remote данные можно заново создать командой `uv run dvc repro`.

## История Git

Работа разделена на ветки `feature/environment`, `feature/dvc-pipeline`
и `docs/readme`. Каждая ветка влита в `main` отдельным merge-коммитом.

```bash
git log --graph --oneline --all
```
