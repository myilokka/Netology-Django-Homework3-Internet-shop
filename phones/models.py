from django.db import models
import psycopg2
from django.urls import reverse
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


