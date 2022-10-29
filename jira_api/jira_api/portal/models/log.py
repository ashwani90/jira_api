from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import Q

User = get_user_model()

class Log(models.Model):
    action=models.CharField(max_length=255)
    data=models.JSONField(null=True)
    time=models.IntegerField(default=0)
    
    def __str__(self):
        return self.action
    
    def create_record(self, action_name,data,time_taken):
        self.objects.create(action=action_name,data=data,time=time_taken)

    def get_server_name(self):
        self.objects.filter(data__content__0__server_name='apache')
        
    def check_key_exists(self):
        self.objects.filter(data__has_key='owner')
        
    def q_objects_example(self):
        self.objects.get(
                Q(action__startswith='task'),
                Q(due_date=date(2005, 5, 2)) | Q(due_date=date(2005, 5, 6))
            )
        
    def delete_task(self):
        self.objects.filter(due_date__year=2005).delete()
        
    def create_copy_of_log(self, data):
        self.create(data)
        self.save()
        self.pk=None
        self._state.adding= True
        self.save()
        
    