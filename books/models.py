from django.db import models

# Create your models here.
# po dokonaniu zmiany w models zrób makemigrate oraz migrate
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    slug = models.SlugField(null=True) # może być pyste w bazie danych (null)


