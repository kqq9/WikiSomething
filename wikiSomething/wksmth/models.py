from django.db import models

class wikiEntry(models.Model):
    search = models.CharField(max_length = 50)
    search_date = models.DateTimeField()
    ip_address = models.CharField(max_length = 39)

    def __str__(self):
        return self.search
