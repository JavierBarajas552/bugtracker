"""BugDoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyUsers.views import login_view, logout_veiw
from Homepage import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_veiw),
    path('submit/', views.submit_ticket_veiw),
    path('user/<int:user_id>', views.user_veiw),
    path('ticket/<int:ticket_id>/edit', views.edit_ticket_veiw),
    path('ticket/<int:ticket_id>', views.ticket_veiw),
    path('claim/<int:ticket_id>', views.claim_ticket),
    path('complete/<int:ticket_id>', views.complete_ticket),
    path('return/<int:ticket_id>', views.return_ticket),
    path('reopen/<int:ticket_id>', views.reopen_ticket),
    path('invalidate/<int:ticket_id>', views.invalidate_ticket),
    path('admin/', admin.site.urls),
]
