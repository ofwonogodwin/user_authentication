from django.urls import path
from .import views

# The urls
urlpatterns = [
    path('',views.register,name = 'registerpage'),
    path('login/',views.login,name = 'loginpage'),
    path('logout/',views.logout,name='logoutpage')
]