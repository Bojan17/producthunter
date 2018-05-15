
from django.db import models
from django.urls import resolve
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def date(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk":self.pk})
