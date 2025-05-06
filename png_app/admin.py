from django.contrib import admin
from .models import UserProfile, NewsArticle, Feedback

# Registering models for Django Admin
admin.site.register(UserProfile)
admin.site.register(NewsArticle)
admin.site.register(Feedback)
