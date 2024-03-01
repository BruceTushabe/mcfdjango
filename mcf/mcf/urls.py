
from django.contrib import admin
from django.urls import path


from core.views import index , contact, upload, generate 


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact' ),
    path('upload/', upload, name='upload'),
    path('generate/', generate, name='generate'),
   

]
