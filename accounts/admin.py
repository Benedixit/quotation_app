from django.contrib import admin
from .models import Cost, Salaries, PriceDetail

# Register your models here.
admin.site.register(Cost)
admin.site.register(Salaries)
admin.site.register(PriceDetail)