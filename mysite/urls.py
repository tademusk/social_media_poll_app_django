from django.contrib import admin
from django.urls import path, include
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('poll.urls')),
    path('test', views.tade )
]
