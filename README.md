# Wallet API project

Проект представляет собой REST API для управления балансом кошельков. Реализованы создание кошелька, операции пополнения и снятия средств, а также проверка баланса.

##  Стек технологий
- Python 3.12
- Django
- PostgreSQL
- Docker и Docker Compose

##  Возможности
1. **POST** `/api/v1/wallets/<WALLET_UUID>/operation` — пополнение или снятие средств.
2. **GET** `/api/v1/wallets/<WALLET_UUID>` — получение текущего баланса.
3. **POST** `/api/v1/wallets/` — создание кошелька.

##  Установка и запуск
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Dontgoingforyou/wallet_proj.git
   cd wallet_proj
   
2. Измените файл .env.example на .env и заполните переменные.
    ```bash
   DB_HOST=db
   DB_PORT=5433
   DB_NAME=wallet
   DB_USER=postgres
   DB_PASSWORD=postgres
   
3. Запустите проект с помощью Docker:
    ```bash
   docker compose up --build
   
4. Приложение будет доступно по адресу:
    ```bash
   http://localhost:8000

5. Для запуска тестов выполните:
    ```bash
   docker compose run app python manage.py test

6. Используйте Postman или curl для проверки эндпоинтов.
   