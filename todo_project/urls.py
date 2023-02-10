from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('post.urls')),
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/usr/', include('UserList.urls')), # new
     path('swagger-ui/',get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),

]
