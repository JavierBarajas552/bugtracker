from django.shortcuts import render, HttpResponseRedirect, reverse
from Homepage.models import TicketModel
from Homepage.forms import SubmitForm, EditForm
from MyUsers.models import MyUser
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    new_tickets = TicketModel.objects.filter(status__exact="New")
    ip_tickets = TicketModel.objects.filter(status__exact="In Progress")
    com_ticktes = TicketModel.objects.filter(status__exact="Done")
    invalid_tickets = TicketModel.objects.filter(status__exact="Invalid")
    return render(request, 'index.html', {'new': new_tickets, 'ip': ip_tickets, 'done':
                                          com_ticktes, 'Inv': invalid_tickets})


@login_required
def user_veiw(request, user_id):
    this_user = MyUser.objects.get(id=user_id)
    sub = TicketModel.objects.filter(
        ticket_filed_by=MyUser.objects.get(id=user_id))
    assigned = TicketModel.objects.filter(
        ticket_assigned_to=MyUser.objects.get(id=user_id))
    com = TicketModel.objects.filter(
        ticket_completed_by=MyUser.objects.get(id=user_id))
    return render(request, "user_veiw.html", {'sub': sub, 'assigned': assigned, 'com': com, 'this_user': this_user})


@login_required
def submit_ticket_veiw(request):
    if request.method == "POST":
        form = SubmitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TicketModel.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                ticket_filed_by=request.user
            )
    form = SubmitForm()
    return render(request, "generic_form.html", {'form': form})


@login_required
def ticket_veiw(request, ticket_id):
    this_ticket = TicketModel.objects.get(id=ticket_id)
    return render(request, "ticket_veiw.html", {'ticket': this_ticket})


@login_required
def edit_ticket_veiw(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=ticket)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = EditForm(instance=ticket)
    return render(request, "generic_form.html", {'form': form})


@login_required
def claim_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.ticket_assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def complete_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.ticket_completed_by = request.user
    ticket.status = 'Done'
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def invalidate_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.ticket_completed_by = request.user
    ticket.status = 'Invalid'
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def reopen_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.ticket_assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def return_ticket(request, ticket_id):
    ticket = TicketModel.objects.get(id=ticket_id)
    ticket.ticket_assigned_to = None
    ticket.status = 'New'
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
