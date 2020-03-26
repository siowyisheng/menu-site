from django.contrib import admin
from django.urls import path

from menu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.ItemsList.as_view()),
    path('menu/<int:pk>/', views.ItemsList.as_view()),
]

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'