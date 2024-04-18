from django.contrib import admin
from django.urls import path
from . import views as v

app_name = "accounts"
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', v.home, name="home"),
    path('create/invoice', v.create_invoice, name="create_invoice"),
    path('edit/invoice/<int:pk>', v.edit_invoice, name="edit_invoice"),
    path('delete/invoice/<int:pk>/', v.delete_invoice, name='delete_invoice'),
    path('summary', v.summary, name="summary"),
    path('invoice/generate/<int:pk>', v.invoice_data, name="invoice_data"),
    path('invoice', v.get_invoice_data, name="get_invoice_data"),
    path('success', v.success, name="success"),
    path('login', v.user_login, name="login"),
    path('register', v.user_registration, name="register"),
    path('logout', v.logout_view, name="logout")
]
