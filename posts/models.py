from django.db import models

from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=244)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
