"""gitall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin

from main import views as mainview

# 
# handlers to handle the 404/403.. requests
# 
from django.conf.urls import (handler400, handler403, handler404)

handler400 = 'main.views.handler400'
handler403 = 'main.views.handler403'
handler404 = 'main.views.handler404'
# handler500 = 'main.views.handler500'

urlpatterns = [
	url(r'^$', mainview.home, name="base"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
