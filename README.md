# Personalised News Generation System

This is a Django-based web application developed for my undergraduate final year project. The main goal of the system is to recommend personalised news articles to users based on their preferences using machine learning techniques.

## Project Overview

The system allows users to register, select their preferred news categories, and receive personalised article recommendations. It makes use of content-based filtering (TF-IDF), collaborative filtering (based on feedback), and a hybrid scoring approach to match users with relevant content.

## Key Features

- User registration and login
- Personalised dashboard showing recommended articles
- Search functionality for browsing articles
- Password reset via email
- Basic admin panel to manage models
- Performance testing with Locust and Chrome DevTools
- Unit and integration tests written with pytest

## Technologies Used

- Python with Django
- SQLite (for database)
- HTML, CSS (for templates)
- pytest (for testing)
- Locust (for performance testing)

## Folder Structure

```
news_generator/
├── manage.py
├── db.sqlite3
├── news_generator/
│   └── settings, urls, wsgi, asgi
├── png_app/
│   ├── templates/
│   ├── static/
│   ├── tests/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── recommender.py
```

## How to Run the Project

1. Make sure Python is installed on your machine.
2. Create and activate a virtual environment.

```bash
python -m venv myenv
myenv\Scripts\activate  # On Windows
```

3. Install required packages.

```bash
pip install -r requirements.txt
```

4. Run database migrations.

```bash
python manage.py migrate
```

5. Start the server.

```bash
python manage.py runserver
```

6. Open the browser and go to `http://127.0.0.1:8000/`

## How to Run Tests

To run the unit and integration tests:

```bash
pytest
```

To run performance tests using Locust:

```bash
locust -f locustfile.py
```

Then visit `http://localhost:8089` in the browser to start the load test.

## Notes

- The system uses dummy data and is not deployed live.
- All recommendations are generated based on user preferences and article content similarity.
- Password reset emails are printed to the console for testing purposes.
