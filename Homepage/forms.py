from django import forms
from django.forms import ModelForm
from Homepage.models import TicketModel


class SubmitForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = ['title', 'description']


class EditForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = ['title', "description", "ticket_filed_by",
                  "status", 'ticket_assigned_to', 'ticket_completed_by']
