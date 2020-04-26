from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

class Manager(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

class Club(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=300)
    text = models.TextField()
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)

class Enrollment(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=130)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    