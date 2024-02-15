from django.urls import path
from .views import enroll,edit,delete
urlpatterns = [
    path('', enroll),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
    
]
