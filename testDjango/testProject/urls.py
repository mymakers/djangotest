from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url="/home/", permanent = True)), #  path에 공백을 넣으면 /home으로 리다이렉트되는 코드. :8000/입력도 :8000/home/ 페이지로 강제이동
    path('user/', include('user.urls')),
]
