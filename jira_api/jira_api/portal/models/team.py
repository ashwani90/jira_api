from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.db.models import F

User = get_user_model()

class Team(models.Model):
    name=models.CharField(max_length=255)
    members=models.ManyToManyField(User, through='Membership')
    
    def __str__(self):
        return self.name
    
    # Add member to many to many field
    def add_member_to_team(self, user_id):
        user=User.objects.get(user_id)
        self.members.add(user)
        
    def add_members_to_team(self, user_ids):
        for i in user_ids:
            user=User.objects.get(i)
            self.members.add(user)
    def get_all_objects(self):
        return self.objects.all()
    def filter_on_data(self, data):
        return self.objects.all().filter(name__contains=data)
    
    def chain_filters(self,first,second,third):
        self.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))
        # q1.exclude(pub_date__gte=datetime.date.today())
        
    def get_team_based_on_username(self,username):
        return self.objects.filter(team__members__name=username)
    
    def append_prefix_to_team_name(self):
        self.objects.update(name="prefix" + F('name') )
    
class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()

