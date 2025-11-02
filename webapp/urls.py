from django.urls import path
from webapp.views import task_list_view
urlpatterns = [
    path('', task_list_view),
]
