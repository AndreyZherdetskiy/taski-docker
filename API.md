# Документация API

## Базовый URL

    http://<host>:8000/api/

---

## Сущность: Задача (Task)

| Поле        | Тип    | Описание                |
|-------------|--------|-------------------------|
| id          | int    | Уникальный идентификатор|
| title       | string | Заголовок задачи        |
| description | string | Описание задачи         |
| completed   | bool   | Статус выполнения       |

---

## Список задач

### Получить список задач
**GET** `/api/tasks/`

**Пример запроса:**
```
curl -X GET http://localhost:8000/api/tasks/
```
**Пример ответа:**
```json
[
  {
    "id": 1,
    "title": "Купить хлеб",
    "description": "Не забыть купить хлеб в магазине",
    "completed": false
  },
  ...
]
```

---

### Создать задачу
**POST** `/api/tasks/`

**Тело запроса:**
```json
{
  "title": "Купить молоко",
  "description": "Взять 2 литра",
  "completed": false
}
```
**Пример запроса:**
```
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко", "description": "Взять 2 литра", "completed": false}'
```
**Пример ответа:**
```json
{
  "id": 2,
  "title": "Купить молоко",
  "description": "Взять 2 литра",
  "completed": false
}
```

**Ошибки:**
- 400 Bad Request — если не переданы обязательные поля или неверный формат данных.

---

### Получить задачу по id
**GET** `/api/tasks/{id}/`

**Пример запроса:**
```
curl -X GET http://localhost:8000/api/tasks/1/
```
**Пример ответа:**
```json
{
  "id": 1,
  "title": "Купить хлеб",
  "description": "Не забыть купить хлеб в магазине",
  "completed": false
}
```

**Ошибки:**
- 404 Not Found — задача не найдена.

---

### Обновить задачу
**PUT** `/api/tasks/{id}/`

**Тело запроса:**
```json
{
  "title": "Купить хлеб и молоко",
  "description": "Взять 2 литра молока и хлеб",
  "completed": true
}
```
**Пример запроса:**
```
curl -X PUT http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить хлеб и молоко", "description": "Взять 2 литра молока и хлеб", "completed": true}'
```
**Пример ответа:**
```json
{
  "id": 1,
  "title": "Купить хлеб и молоко",
  "description": "Взять 2 литра молока и хлеб",
  "completed": true
}
```

**Ошибки:**
- 400 Bad Request — неверный формат данных.
- 404 Not Found — задача не найдена.

---

### Частичное обновление задачи
**PATCH** `/api/tasks/{id}/`

**Тело запроса:**
```json
{
  "completed": true
}
```
**Пример запроса:**
```
curl -X PATCH http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```
**Пример ответа:**
```json
{
  "id": 1,
  "title": "Купить хлеб",
  "description": "Не забыть купить хлеб в магазине",
  "completed": true
}
```

---

### Удалить задачу
**DELETE** `/api/tasks/{id}/`

**Пример запроса:**
```
curl -X DELETE http://localhost:8000/api/tasks/1/
```
**Пример ответа:**
```json
{
  "id": 1,
  "title": "Купить хлеб",
  "description": "Не забыть купить хлеб в магазине",
  "completed": false
}
```

**Ошибки:**
- 404 Not Found — задача не найдена.

---

## Примечания
- Все ответы и запросы используют формат JSON.
- Все поля обязательны, кроме id (он генерируется автоматически).
- Других эндпоинтов, кроме /api/tasks/, нет.
 