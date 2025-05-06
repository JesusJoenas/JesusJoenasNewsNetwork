import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_register_view(client):
    response = client.post(reverse('register'), {
        'username': 'newuser123',
        'first_name': 'First',
        'last_name': 'Last',
        'email': 'newuser123@example.com',
        'preferred_categories': 'technology, sports, health',  
        'password1': 'VeryStrongPass123!',
        'password2': 'VeryStrongPass123!'
    })
    assert response.status_code == 302  # Redirect to login page
