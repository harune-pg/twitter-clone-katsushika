from django.urls import path, include

from . import views


app_name = 'accounts'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='singup'),
]
