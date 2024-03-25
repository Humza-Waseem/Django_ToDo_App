from django.db import models
from django.contrib.auth.models import User   # the user model takes care of our User Info like username, password, email, etc

# Create your models here.

class Task(models.Model):
    title  = models.CharField(max_length=150)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length = 250,blank = True, null = True) # the blank and null will allow the description to be optional (not required
    dueDate = models.DateTimeField(null = True, blank = True) # this will be the date and time when the task is due
    # priority =
    created = models.DateTimeField(auto_now_add = True)# the auto_now_add will automatically add the date and time when the task is created
    complete = models.BooleanField(default = False) # setting the default of this to false because when we first create a task it is not completed
     
    REQUIRED_FIELDS = [title,complete]
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete', '-created'] # created will set the order of the tasks to be in the order of the date and time they were created in ascending order
    