from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Topic of user's interest."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns model representation as a string."""
        return self.text

class Entry(models.Model):
    """Detailed information about learning progress."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns model representation as a string."""
        return f"{self.text[:50]}..."