import pytest

@pytest.mark.django_db
def test_register_and_login(client):
    # Register
    response = client.post('/register/', {
        'username': 'integrationuser123',
        'first_name': 'Integration',
        'last_name': 'User',
        'email': 'integrationuser123@example.com',
        'preferred_categories': 'technology, sports, health',  
        'password1': 'ComplexPass456!',
        'password2': 'ComplexPass456!'
    })
    assert response.status_code == 302  # Redirect after successful register

    # Login
    login_response = client.post('/login/', {
        'username': 'integrationuser123',
        'password': 'ComplexPass456!'
    })
    assert login_response.status_code == 302  # Redirect after successful login
