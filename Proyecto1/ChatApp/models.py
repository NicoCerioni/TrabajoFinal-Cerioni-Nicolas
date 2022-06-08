from django.db import models

class chat_message(models.Model):
    message = models.TextField()
    emisor = models.CharField(max_length=50)
    receptor = models.CharField(max_length=50)
    date = models.DateTimeField(default=None)
    def __str__(self):
        return self.message
