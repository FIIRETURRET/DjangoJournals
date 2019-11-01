from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length=100)
    journal_entry = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='journals', on_delete=models.PROTECT)
