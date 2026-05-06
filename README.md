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
   `git clone https://github.com`
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
