from django.urls import path
from .views import RegisterUser, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
]
