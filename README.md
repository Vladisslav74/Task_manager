english versions
# Django Task Manager API

A robust Backend Task Management system built with **Django** and **Django Rest Framework**. 
This project provides a full CRUD REST API to manage your daily tasks.

## Features
*   **Full CRUD**: Create, Read, Update, and Delete tasks.
*   **Priority System**: Tasks are sorted by priority (1-5).
*   **REST API**: Integrated Browsable API by DRF.
*   **Filtering**: Separate endpoints for urgent and completed tasks.

## Tech Stack
*   Python 3.x
*   Django 5.0
*   Django Rest Framework
*   SQLite

## Installation & Setup
1. **Clone the repository:**
   `git clone https://github.com/Vladisslav74/Task_manager`
2. **Set up a virtual environment:**
   `python -m venv .venv`
   `source .venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. **Install dependencies:**
   `pip install django djangorestframework`
4. **Run migrations:**
   `python manage.py migrate`
5. **Start the server:**
   `python manage.py runserver`

## API Endpoints
*   `GET /api/v1/tasks/` - View all active tasks.
*   `POST /api/v1/tasks/` - Create a new task.
*   `GET/PUT/DELETE /api/v1/tasks/<id>/` - Manage a specific task.

русская версия
# Django Task Manager API

Надежная система управления задачами на бэкэнде, созданная с использованием **Django** и **Django Rest Framework**.
Этот проект предоставляет полноценный CRUD REST API для управления вашими ежедневными задачами.

## Функции
*   **Полный набор функций CRUD**: создание, чтение, обновление и удаление задач.
*   **Система приоритетов**: Задачи сортируются по приоритету (1-5).
*   **REST API**: Встроенный браузерный API от DRF.
*   **Фильтрация**: Отдельные эндпоинты для срочных и завершенных задач.

## Технический стек
*   Python 3.x
*   Django 5.0
*   Django Rest Framework
*   SQLite

## Установка и Настройки
1. **Клонировать репозиторий:**
   `git clone https://github.com/Vladisslav74/Task_manager`
2. **Создать виртуальную среду:**
   `python -m venv .venv`
   `source .venv/bin/activate` (или `venv\Scripts\activate` на Windows)
3. **Установить зависимости:**
   `pip install django djangorestframework`
4. **Запустить миграции:**
   `python manage.py migrate`
5. **Запустить сервер:**
   `python manage.py runserver`

## API эндпоинты
*   `GET /api/v1/tasks/` - Посмотреть все активные задачи.
*   `POST /api/v1/tasks/` - Создать новую задачу.
*   `GET/PUT/DELETE /api/v1/tasks/<id>/` - Управлять определенной задачей
