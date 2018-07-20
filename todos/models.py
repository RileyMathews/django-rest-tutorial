from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gamertag = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        """ A string representation of the model. """
        return self.gamertag

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.title

