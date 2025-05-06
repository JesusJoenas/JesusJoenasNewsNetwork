from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, FeedbackForm
from .recommender import recommend_news
from .utils import fetch_all_articles

# Home page
def home(request):
    query = request.GET.get('q')
    articles = fetch_all_articles(query) if query else fetch_all_articles('breaking')
    return render(request, 'png_app/home.html', {'articles': articles})

# About page
def about_page(request):
    return render(request, 'png_app/about.html')

# Dashboard
@login_required
def dashboard(request):
    user_profile = request.user
    query = request.GET.get('query', '')

    if query:
        articles = fetch_all_articles(query)
    else:
        articles = recommend_news(user_profile)
        if not articles:
            articles = fetch_all_articles('latest')  # fallback to latest

    context = {
        'first_name': user_profile.first_name,
        'articles': articles
    }
    return render(request, 'png_app/dashboard.html', context)

# Register user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'png_app/register.html', {'form': form})

# Login user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'png_app/login.html')

# Logout user
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# Search articles
@login_required
def search(request):
    query = request.GET.get('query', '')
    articles = fetch_all_articles(query)
    return render(request, 'png_app/search.html', {'articles': articles})

# Feedback page
@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            messages.success(request, "Thanks for your feedback!")
            return redirect('dashboard')
    else:
        form = FeedbackForm()
    
    return render(request, 'png_app/feedback.html', {'form': form})
