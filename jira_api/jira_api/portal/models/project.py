from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Project(models.Model):
    
    STATUSES = (
        ('0', 'Active'),
        ('1', 'Paused'),
        ('2', 'Completed'),
    )
    
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, null=True)
    budget = models.IntegerField(default=None)
    status = models.CharField(max_length=1, choices=STATUSES)
    due_date = models.DateField(default=None)
    started_on = models.DateField(default=None)
    users = models.ManyToManyField(
        User, default=None
    )
    
    class Meta:
        ordering= ['name']
        verbose_name_plural = "projects"
        
    # Define custom methods on a model to add custom “row-level” functionality to your objects.
    # Whereas Manager methods are intended to do “table-wide” things, model methods should act on a particular model instance.
    def project_status(self) -> bool:
        return True
    
    @property
    def get_project_budjet(self) -> str:
        return "$%s" % (self.budget)
    
    def __str__(self) -> str:
        return super().__str__()
