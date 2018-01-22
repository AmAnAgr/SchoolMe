from django.contrib import admin
from .models import School, User, Feedback


# Register your models here.
admin.site.register(School)
admin.site.register(User)
admin.site.register(Feedback)