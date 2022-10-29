from django.db import models
from .module import Module
from django.contrib.auth import get_user_model
from django.db.models import F
from datetime import timedelta
from django.db.models import Min
from django.db.models import OuterRef, Subquery, Sum
from django.db.models import Avg, Max, FloatField, Count
from django.db import connection


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
    
    def save(self, *args, **kwargs):
        self.status=0
        super().save(*args, **kwargs)  
        
    def filter_on_year(self):
        return self.objects.filter(due_date__year=2008)
    
    def get_invalid_tasks(self):
        return self.objects.filter(due_date__lt=F('started_on'))
    
    def get_projects_on_time_difference(self):
        return self.objects.filter(due_date__lt=F('due_date') + timedelta(days=3))
    
    def get_lowest_status(self):
        self.objects.aggregate(status=Min('status'))
        
    def get_data_using_subquery(self):
        return self.objects.values('due_date__year').annotate(top_rating=Subquery(
             self.objects.filter(
                 due_date__year=OuterRef('due_date__year'),
             ).order_by('-status').values('status')[:1]
            ),
            total_users=Sum('user'),
            )
        
    def get_tasks(self, list):
        self.objects.filter(pk__in=list)
        
    def skip_percentage(self):
        self.objects.filter(name__contains='%')
        
    # def get_user_asynchronously(self, username):
    #     user = await User.objects.filter(username=username).afirst()
    
    def get_due_date_null(self):
        self.objects.filter(data__isnull=True)
    
    @property
    def get_task_name(self) -> str:
        return "$%s" % (self.name)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def count_tasks(self):
        return self.objects.count()

    def get_average(self):
        return self.objects.aggregate(Avg('id'))
        
    def get_max_id(self):
        return self.objects.aggregate(Max('id'))
        
    def get_difference(self):
        return self.objects.aggregate(price_diff=Max('id', output_field=FloatField()) - Avg('id'))
    
    # generate aggregate over a queryset
    def aggregate_over_queryset(self):
        return self.objects.all().aggregate(Avg('id'))
    
    def count_multiple(self):
        q=self.objects.annotate(Count('id', distinct=True), Count('name', distinct=True))
        return q[0].id__count
    
    def execute_raw_query(self):
        list=[]
        for p in self.objects.raw('SELECT * FROM myapp_person'):
            list.append(p)
        return list
    
    def calling_stored_procedure(self):
        with connection.cursor() as cursor:
            cursor.callproc('test_procedure', [1, 'test'])