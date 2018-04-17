from django.conf.urls import url

from AppTwo import views

urlpatterns=[

    url(r'^users/', views.users, name='users'),
    url(r'^$', views.help, name='help'),
]
