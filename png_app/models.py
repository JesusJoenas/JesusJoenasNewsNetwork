from django.db import models
from django.contrib.auth.models import User

# Model to extend the user profile with preferred news categories
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_categories = models.CharField(max_length=200, help_text="Comma-separated list of preferred categories.")

    def __str__(self):
        return self.user.username

# Model to represent a news article
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Model to capture user feedback on articles
class Feedback(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(1, 'Dislike'), (2, 'Neutral'), (3, 'Like')])

    def __str__(self):
        return f"{self.user.username} - {self.article.title} ({self.rating})"
