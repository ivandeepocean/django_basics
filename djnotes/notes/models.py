from django.db import models

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=512, blank = True)
    note = models.TextField(blank=True)
    notetest = models.TextField(blank=True)

    def _str_(self):
        return self.title
