from django.contrib import admin
from django.urls import path, include
from core.views import index, contact, upload, generate, populate_excel_view, success_view

app_name = 'core'

urlpatterns = [
    #path('core/', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('upload/', upload, name='upload'),
    path('loan_form/', populate_excel_view, name='populate_excel'),
    path('success/', success_view, name='success'),
    path('generate/', generate, name='generate'),

    path("__debug__/", include("debug_toolbar.urls")),  # Include Django Debug Toolbar URL pattern
]
