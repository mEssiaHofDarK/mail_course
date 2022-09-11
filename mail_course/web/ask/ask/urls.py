"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
# from django.urls import include
from qa.views import (
    test,
    main,
    popular,
    question,
)

urlpatterns = [
    # url(r'admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^popular/', popular, name='popular'),
    url(r'^question/([0-9]+)/', question, name='question'),
    url(r'^ask/', test, name='test'),
    url(r'^new/', test, name='test'),
    url(r'^login/', test, name='test'),
    url(r'^signup/', test, name='test'),
]
