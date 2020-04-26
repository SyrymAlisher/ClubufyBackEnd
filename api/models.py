from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

class Club(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=30)
    text = models.TextField()
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
