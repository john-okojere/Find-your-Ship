from django.db import models
from user.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    A_picture_of_Daddie = models.ImageField(upload_to="pic/")
    message = models.TextField(max_length=255)
    date_added = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        f'{self.name.title()}'