from django.db import models


class Sostav(models.Model):
    FIO = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sostav/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
