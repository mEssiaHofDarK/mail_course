from django.contrib import admin
from django.conf.urls import url
from .views import (
    test,
    main,
    popular,
    question,
)

urlpatterns = [
    # path(r'admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^popular', popular, name='popular'),
    url(r'^question/[0-9]+/', question, name='question'),
    url(r'^ask/', test, name='test'),
    url(r'^new/', test, name='test'),
    url(r'^login/', test, name='test'),
    url(r'^signup/', test, name='test'),
]
