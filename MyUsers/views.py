from django.shortcuts import render, HttpResponseRedirect, reverse
from MyUsers.models import MyUser
from MyUsers.forms import LoginForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if MyUser:
                login(request, MyUser)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


def logout_veiw(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
