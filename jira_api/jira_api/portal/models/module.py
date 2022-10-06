from django.db import models
from .project import Project

class Module(models.Model):
    
    STATUSES = (
        ('0', 'Active'),
        ('1', 'Paused'),
        ('2', 'In Progress'),
        ('2', 'Completed'),
    )
    
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES)
    due_date = models.DateField(default=None)
    started_on = models.DateField(default=None)
    
    class Meta:
        ordering= ['name']
        verbose_name_plural = "modules"
        
    # Define custom methods on a model to add custom “row-level” functionality to your objects.
    # Whereas Manager methods are intended to do “table-wide” things, model methods should act on a particular model instance.
    def module_status(self) -> bool:
        return True
    
    @property
    def get_module_name(self) -> str:
        return "$%s" % (self.name)
    
    def __str__(self) -> str:
        return super().__str__()
    
