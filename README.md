# Kittygram - Социальная сеть для обмена фотографиями питомцев

## Описание проекта
Kittygram - это веб-приложение, созданное по аналогии с Instagram, но с фокусом на фотографиях домашних питомцев. Проект включает в себя полнофункциональный бэкенд на Django и интегрированный фронтенд на React.

## Особенности проекта
- Публикация фотографий питомцев
- Система достижений для владельцев
- Управление профилем пользователя
- Работа с изображениями в формате base64
- Детальная настройка прав доступа
- Пагинация контента

## Технологии
- Python, Django
- React.js
- Docker
- Nginx
- Gunicorn
- PostgreSQL

## Структура проекта
```
.
├──.github
├── backend
├── frontend
├── nginx
├── tests
├──.env.example
├──.gitignore
├── 
├── docker-compose.production.yml
├── docker-compose.yml
├── kittygram_workflow.yml
├── pytest.ini
├── setup.cfg
└── tests.yml
```
## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
##API Endpoints
###Котики
```
GET /api/cats/ - Получить список котиков
POST /api/cats/ - Создать нового котика
GET /api/cats/{id}/ - Получить конкретного котика
PUT /api/cats/{id}/ - Обновить информацию о котике
DELETE /api/cats/{id}/ - Удалить котика
```
###Достижения
```
GET /api/achievements/ - Получить список достижений
POST /api/achievements/ - Создать новое достижение
GET /api/achievements/{id}/ - Получить конкретное достижение
PUT /api/achievements/{id}/ - Обновить достижение
DELETE /api/achievements/{id}/ - Удалить достижение
```
##Тестирование
Для запуска тестов:
```
python manage.py test
```
##Деплой
Проект настроен для деплоя через Docker-контейнеры:

```
docker-compose up -d
```
