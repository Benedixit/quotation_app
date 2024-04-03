from django.contrib import admin
from .models import Cost, Salaries, PriceDetail, PriceInclude

# Register your models here.
admin.site.register(Cost)
admin.site.register(Salaries)
admin.site.register(PriceDetail)
admin.site.register(PriceInclude)