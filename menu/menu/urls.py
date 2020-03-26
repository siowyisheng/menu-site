from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from menu_app import views

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('menu/', views.ItemsList.as_view()),
    path('menu/<int:pk>/', views.ItemsList.as_view()),
    path('item/<int:pk>/', views.ItemCreateUpdateDelete.as_view()),
    path('category/', views.CategoryCreate.as_view()),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'