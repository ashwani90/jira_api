from django.db import models
from .module import Module
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    
    STATUSES = (
        ('0', 'Active'),
        ('1', 'Paused'),
        ('2', 'In Progress'),
        ('2', 'Completed'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=1, choices=STATUSES, default=1)
    due_date = models.DateField(default=None)
    started_on = models.DateField(default=None)
    
    class Meta:
        ordering= ['name']
        verbose_name_plural = "modules"
        
    def module_status(self) -> bool:
        return True
    
    @property
    def get_task_name(self) -> str:
        return "$%s" % (self.name)
    
    def __str__(self) -> str:
        return super().__str__()
    
