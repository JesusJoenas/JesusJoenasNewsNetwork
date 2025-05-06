import pytest
from png_app.forms import UserRegisterForm

@pytest.mark.django_db
def test_user_register_form_valid():
    form = UserRegisterForm(data={
        'username': 'testuser123',
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser123@example.com',
        'preferred_categories': 'technology, sports, health',  
        'password1': 'StrongPass123!',
        'password2': 'StrongPass123!'
    })
    if not form.is_valid():
        print(form.errors)
    assert form.is_valid()
