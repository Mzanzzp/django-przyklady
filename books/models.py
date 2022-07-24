from django.db import models

# Create your models here.
# po dokonaniu zmiany w models zrób makemigrations oraz migrate
from django.template.defaultfilters import slugify


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    slug = models.SlugField(null=True) # może być pyste w bazie danych (null)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
        )