# 🚀 AI Automation Journey — Quote Bot & API

Этот проект — полноценный backend-приложение с Telegram-ботом и FastAPI API.
Он демонстрирует современную архитектуру backend-разработки с разделением на слои (Layered Architecture).

---

## 📌 Возможности

* 🤖 Telegram-бот с командами:

  * `/start` — регистрация пользователя
  * `/quote` — получить случайную цитату
  * `/history` — история цитат
  * `/help` — список команд

* 🌐 FastAPI сервер:

  * `GET /` — проверка работы сервера
  * `GET /quote` — получить случайную цитату

* 💾 База данных (SQLite + SQLAlchemy):

  * хранение пользователей
  * хранение цитат
  * история запросов

* 🔄 Fallback логика:

  1. Получение цитаты с внешнего API
  2. Если не работает — запрос к локальному API
  3. Если нет данных — сообщение об ошибке

---

## 🏗 Архитектура проекта

Проект построен по принципу слоёв:

API → Service → Database

```text
app/
 ├── api/         # FastAPI endpoints
 ├── bot/         # Telegram bot
 ├── core/        # конфигурация
 ├── database/    # модели и работа с БД
 ├── services/    # бизнес-логика и API
 └── main.py      # точка входа FastAPI
```

---

## ⚙️ Установка и запуск

### 1. Клонировать проект

```bash
git clone <your-repo-url>
cd ai-automayiom-journey
```

---

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Создать `.env`

```env
TELEGRAM_TOKEN=your_telegram_token
```

---

## ▶️ Запуск

### 🔹 Запуск FastAPI сервера

```bash
uvicorn app.main:app --reload
```

Проверка:

```text
http://127.0.0.1:8000/docs
```

---

### 🔹 Запуск Telegram-бота

```bash
python -m app.bot.telegram_bot
```

---

## 🧠 Как это работает

1. Пользователь пишет `/quote` в Telegram
2. Бот вызывает сервис
3. Сервис:

   * пытается получить цитату из внешнего API
   * если не получается — обращается к локальному API
4. Цитата сохраняется в базу данных
5. Пользователь получает ответ

---

## 📊 Используемые технологии

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* python-telegram-bot
* httpx
* python-dotenv

---

## 🔥 Особенности

* Чистая архитектура (separation of concerns)
* Асинхронные запросы (async/await)
* Логирование ошибок
* Готовность к переходу на PostgreSQL
* Подготовка к масштабированию (microservices)

---

## 🚀 Дальнейшее развитие

* PostgreSQL вместо SQLite
* Alembic миграции
* Docker
* Разделение на микросервисы
* Деплой (Render / Railway / AWS)

---

## 👩‍💻 Автор

Проект выполнен в рамках обучения backend-разработке и построения production-ready приложений.
