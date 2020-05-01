from django.db import models

class wikiEntry(models.Model):
    search = models.CharField(max_length = 50)
    search_date = models.DateTimeField()

    def __str__(self):
        return self.search
