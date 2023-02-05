from django.urls import path
from gitlearning.views import index_page_view

urlpatterns = [
    path('', index_page_view, name='home'),
]