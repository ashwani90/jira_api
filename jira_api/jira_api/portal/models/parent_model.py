from django.db import models

class ParentModel(models.Model):
    created_on = models.DateField()
    updated_on = models.DateField()

    # We can override meta options in concrete model
    class Meta:
        abstract = True