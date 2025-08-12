from django.urls import path
from . import views
from django.contrib import admin

app_name="tapal"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('login', views.login, name='login'),
    # path('signup', views.signUp, name='signup'),
    # path('new-ticket', views.newTicket, name='new-ticket'),
    # path('view-ticket', views.viewTicket, name='view-ticket'),
]
