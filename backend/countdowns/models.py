from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class CountdownQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    
class CountdownManager(models.Manager):
     def get_queryset(self, *args, **kwargs):
        return CountdownQuerySet(self.model, using=self._db)
     
class Countdown(models.Model):
    name = models.CharField(max_length=120)
    target_time = models.DateTimeField()
    user = models.ForeignKey(User,default=1,null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    public = models.BooleanField(default=True)

    objects = CountdownManager()
    def __str__(self):
        return self.name