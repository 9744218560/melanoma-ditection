
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', Login.as_view() , name='login'),
    path('Logout', Logout.as_view() , name='Logout'),
    path('complaints', ComplaintsView.as_view() , name='complaints'),
    path('feedback', feedback.as_view() , name='feedback'),
    path('Home', Home.as_view() , name='Home'),
    path('manage_user', manage_user.as_view() , name='manage_user'),
    path('accept_user/<int:lid>', accept_user.as_view() , name='accept_user'),
    path('rejected_user/<int:lid>', rejected_user.as_view() , name='rejected_user'),

]
