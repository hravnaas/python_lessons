from django.conf.urls import url
from . import views

def index(request):
	print("I'm running")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index)
]