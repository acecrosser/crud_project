from django.db import models
from users.models import User


class Crud(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='Crud', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

