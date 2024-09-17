from django.db import models
from datetime import date

class todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished = models.DateField(null=True)

    class Meta:
       ordering = ["deadline"]


    def  mark_has_complete(Self): 
         if not Self.finished:
             Self.finished = date.today() 
             Self.save()