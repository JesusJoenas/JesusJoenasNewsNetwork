# Jesus Joenas News Network (JJNN)

Jesus Joenas News Network (JJNN) is a personalized news delivery platform built using Django and machine learning. The main goal of the system is to recommend personalised news articles to users based on their preferences, ensuring users receive relevant and meaningful updates.

## Project Overview

The system allows users to register, select their preferred news categories, and receive personalised article recommendations. It makes use of content-based filtering (TF-IDF), collaborative filtering (based on feedback), and a hybrid scoring approach to match users with relevant content.

## Key Features

- User registration and login
- Machine learning recommendations (content-based, collaborative + hybrid)
- Personalised dashboard showing recommended articles
- Search functionality for browsing articles by keyword
- Password reset via email
- Basic admin panel to manage models
- Performance testing with Locust and Chrome DevTools
- Unit and integration tests were carried out using black-box and white-box techniques

## Testing Overview

- Unit tests (views, forms, recommender logic)
- Black-box testing (input validation, login errors)
- White-box testing (branch, path, statement coverage)
- Integration testing with `pytest`
- Load testing via [Locust](https://locust.io/)
- Performance tracked using Chrome DevTools

## 🛠 Technologies used

- Backend: Django
- Frontend: HTML + CSS (Django Templates)
- Database: SQLite
- ML Model: TF-IDF + hybrid recommender (Python)
- Testing: Pytest, Unittest, Locust, Chrome DevTools

## Screenshots

| Filename                        | Description                                                              |
|--------------------------------|--------------------------------------------------------------------------|
| `homepage_news_feed.png`       | Homepage showing top news articles                                       |
| `register_required_field.png`  | Registration form highlighting required field                            |
| `register_invalid_input.png`   | Error shown for invalid registration inputs                              |
| `register_validation_errors.png`| Password/category validation messages                                    |
| `dashboard_welcome_user.png`   | Logged-in user's personalized dashboard                                  |
| `homepage_logged_out.png`      | Homepage after logout with session cleared                               |
| `password_reset_form.png`      | Email input for password reset                                           |
| `login_invalid_credentials.png`| Login error for incorrect credentials                                    |
| `password_reset_email.png`     | Preview of reset email and link                                          |
| `new_password_entry.png`       | Form for setting a new password                                          |
| `password_reset_success.png`   | Success message confirming password reset                                |
| `pytest_test_results.png`      | Pytest results showing all tests passed                                  |
| `chrome_devtools_network.png`  | Chrome DevTools performance breakdown                                    |
| `locust_stats_overview.png`    | Stats from Locust performance test                                       |
| `locust_requests_chart.png`    | Requests per second graph from Locust load test                          |

> These screenshots highlight major features, authentication flow, and performance metrics from testing.

---

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


---

## Contact

Built by Jesus Joenas  
💼 [GitHub](https://github.com/JesusJoenas)  
📧 Reach out for collaboration, improvements, or code review!


