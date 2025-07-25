from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, 
                            on_delete=models.CASCADE, 
                            related_name='expenses_categories',
                            null=True,
                            blank=True)
    name = models.CharField(max_length=120,unique=True)
    description = models.TextField(blank=True,null=True)
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, 
                            on_delete=models.CASCADE, 
                            related_name='transactions',
                            null=True,
                            blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,
                                 related_name='transactions',null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date','-created_at']

    def __str__(self):
        return f"{self.user.username}'s {self.amount} on {self.date} for {self.category or 'uncategorized'}"
