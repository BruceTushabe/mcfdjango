from django.contrib import admin
from django.urls import path, include
from core.views import index , contact, upload, generate, populate_excel_view, success_view

APP_NAME = 'core'

urlpatterns = [
    #path('', include('core.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact' ),
    path('upload/', upload, name='upload'),
    path('generate/', generate, name='generate'),
    path('loan_form/', populate_excel_view, name='populate_excel'),
    path('success/', success_view, name='success'),
    path("__debug__/", include("debug_toolbar.urls")),
]
