from django.db import models
from MyUsers.models import MyUser
# Create your models here.


class TicketModel(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateField(auto_now=True)
    description = models.TextField()
    ticket_filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='New', choices=[(
        "New", 'New'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')])
    ticket_assigned_to = models.ForeignKey(
        MyUser, null=True, blank=True, related_name='Clamed_by', on_delete=models.CASCADE)
    ticket_completed_by = models.ForeignKey(
        MyUser, null=True, blank=True, related_name='Completed_by', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
