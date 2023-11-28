from django.db import models
from datetime import datetime

# Create your models here.


class NotesGroup(models.Model):
    title = models.CharField(null=False, max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Note(models.Model):
    title = models.CharField(null=False, max_length=50)
    date = models.DateField(default=datetime.now())
    content = models.TextField()
    notes_group = models.ForeignKey(NotesGroup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    