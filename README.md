# 📜 Quotes Telegram Bot

Telegram-бот для получения случайных цитат с сохранением истории пользователей.
Проект реализован с использованием FastAPI, SQLAlchemy и внешнего API.

---

## 🚀 Функциональность

* 📩 Получение случайной цитаты (`/quote`)
* 💾 Сохранение истории цитат пользователя
* 📜 Просмотр последних цитат (`/history`)
* 🔄 Резервный источник цитат (локальный API)
* 👤 Автоматическое создание пользователя
* ⚡ Асинхронная работа с API

---

## 🧱 Архитектура проекта

```
app/
├── bot/            # Telegram-бот
├── api/            # FastAPI маршруты
├── database/       # модели, CRUD, подключение к БД
├── services/       # работа с внешними API
├── core/           # конфигурация
```

---

## 🛠️ Технологии

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite / PostgreSQL
* httpx (async HTTP)
* python-telegram-bot
* Render (деплой)

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Создать виртуальное окружение

```
python -m venv .venv
```

Активировать:

```
.venv\Scripts\activate
```

### 3. Установить зависимости

```
pip install -r requirements.txt
```

---

### 4. Настроить переменные окружения

Создать файл `.env`:

```
TELEGRAM_TOKEN=your_token_here
DATABASE_URL=sqlite:///./quotes.db
```

---

### 5. Запустить API

```
uvicorn app.main:app --reload
```

API будет доступен:

```
http://127.0.0.1:8000
```

---

### 6. Запустить Telegram-бота

```
python -m app.bot.telegram_bot
```

---

## 🤖 Команды бота

* `/start` — начать работу
* `/quote` — получить случайную цитату
* `/history` — посмотреть историю цитат
* `/help` — список команд

---

## 🌐 Источники цитат

1. Внешний API:

   * https://api.quotable.io/random

2. Локальный сервер (fallback):

   * `/quote` endpoint FastAPI

---

## ☁️ Деплой

Проект задеплоен на Render:

* API: `https://your-api-url.onrender.com`
* Бот: Background Worker

---

## ⚠️ Особенности

* Используется fallback-логика при недоступности внешнего API
* Поддержка как SQLite (локально), так и PostgreSQL (в продакшене)
* Разделение логики на слои (bot / services / database)

---

## 📚 Чему научился

* Работа с FastAPI
* Асинхронные HTTP-запросы (httpx)
* Архитектура backend-проекта
* Работа с базой данных через SQLAlchemy
* Интеграция Telegram-бота
* Деплой на Render
* Обработка ошибок и fallback-логика

---

## 📌 Планы по развитию

* Добавить категории цитат
* Реализовать поиск по автору
* Добавить лайки/избранное
* Подключить кэширование

---

## 👩‍💻 Автор

Разработано в рамках обучения backend-разработке 🚀
