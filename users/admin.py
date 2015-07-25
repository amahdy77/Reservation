from django.contrib import admin
from .models import ExpectedUser

# Register your models here.

class ExpectedUserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'guests', 'registration']

    class Meta:
        model = ExpectedUser

admin.site.register(ExpectedUser, ExpectedUserAdmin)
