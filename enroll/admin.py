from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class studentregister(admin.ModelAdmin):
    list_display=('pk','name','email')