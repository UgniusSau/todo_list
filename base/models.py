import uuid
from django.db import models
from django.contrib.auth.models import User




class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add = True)
    start_date = models.DateField(blank= True,null=True)
    start_date_time = models.TimeField(blank= True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_date_time = models.TimeField(blank= True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete','end_date', 'end_date_time']
