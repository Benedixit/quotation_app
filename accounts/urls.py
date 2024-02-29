from django.contrib import admin
from django.urls import path
from . import views as v



app_name = "accounts"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name="home"),
    path('summary', v.summary, name="summary"),
    path('invoice', v.invoice_summary, name="invoice"),
    path('success', v.success, name="success")
]
