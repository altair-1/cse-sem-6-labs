from django.urls import include, re_path
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path(r'^admin/', admin.site.urls),
    re_path('', views.index, name='basic'),
]