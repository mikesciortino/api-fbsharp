from django.urls import include, path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('players.urls')),
    path('ranks/',  include('ranks.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
