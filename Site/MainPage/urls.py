from django.urls import path
from .views import mainView

app_name = 'Tweets'
urlpatterns = [
    path('', mainView),
]