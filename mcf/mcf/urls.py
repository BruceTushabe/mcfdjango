from django.contrib import admin
from django.urls import path, include
from core import views as core_views

#app_name = 'core'

urlpatterns = [
    path('', core_views.index, name='index'),
    path('contact/', core_views.contact, name='contact'),
    path('upload/', core_views.upload, name='upload'),
    path('loan_form/', core_views.populate_excel_view, name='populate_excel'),
    path('success/', core_views.success_view, name='success'),
    path('generate/', core_views.generate, name='generate'),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),  # Include Django Debug Toolbar URL pattern
]
