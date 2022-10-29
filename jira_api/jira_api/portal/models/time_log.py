from django.db import models
from .task import Task

class TimeLog(models.Model):
    value=models.IntegerField(default=0)
    unit=models.CharField(max_length=255,default=None)
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.value
    
class NewManager(models.Manager):
    pass

    
class MyTimeLog(TimeLog):
    objects = NewManager()
    class Meta:
        proxy = True

    def do_something(self):
        pass