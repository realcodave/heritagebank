from django.contrib import admin
from .models import Statement, Amount
# Register your models here.
admin.site.register(Statement)
admin.site.register(Amount)