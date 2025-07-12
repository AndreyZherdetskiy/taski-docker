# Taski

## Описание

Taski — это простой таск-трекер с API на Django и фронтендом на React, развёрнутый в Docker-контейнерах. Проект позволяет создавать, просматривать, редактировать и удалять задачи через REST API. Вся инфраструктура полностью контейнеризирована (backend, frontend, gateway, db).

## Технологии
- Python 3.9+
- Django 3.2+
- Django REST Framework
- PostgreSQL
- Docker, docker-compose
- Nginx (gateway)
- React (frontend)

## Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:AndreyZherdetskiy/taski-docker.git
   cd taski-docker
   ```
2. Скопируйте пример переменных окружения и настройте свой `.env`:
   ```bash
   cp .env.example .env
   # или создайте вручную и заполните переменные ниже
   ```
3. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build
   ```
4. API будет доступен по адресу: [http://localhost:8000/api/](http://localhost:8000/api/)

## Структура репозитория

```
backend/        # Django backend (API, миграции, модели)
frontend/       # Фронтенд (React, компоненты, стили)
gateway/        # Nginx-конфиг для проксирования и отдачи статики
docker-compose.yml  # Основной docker-compose файл
.env            # Переменные окружения (создаётся вручную)
API.md          # Документация по API
```

## Переменные окружения

- `DJANGO_SECRET_KEY` — секретный ключ Django
- `DJANGO_DEBUG` — режим отладки (True/False)
- `DJANGO_ALLOWED_HOSTS` — список разрешённых хостов
- `POSTGRES_DB` — имя БД
- `POSTGRES_USER` — пользователь БД
- `POSTGRES_PASSWORD` — пароль БД
- `POSTGRES_HOST` — адрес БД (обычно `db`)
- `POSTGRES_PORT` — порт БД (обычно 5432)

## Основные команды

- Запуск контейнеров: `docker-compose up --build`
- Остановка: `docker-compose down`
- Просмотр логов: `docker-compose logs backend`
- Применение миграций вручную: `docker-compose exec backend python manage.py migrate`

## Документация API

Полная документация с примерами: [API.md](./API.md)

## Авторы
- [Andrey Zherdetskiy](https://github.com/AndreyZherdetskiy)

## Лицензия
MIT
