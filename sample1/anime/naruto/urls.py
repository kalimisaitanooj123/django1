"""anime URL Configuration

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

from django.urls import path
from naruto import views


urlpatterns = [
    path("", views.uzumaki,name="q"),

    path("1", views.uzumaki2, name="qs"),
    path("2", views.uzumaki3,name="qsw"),
    path("3", views.uzumaki4,name="qswe"),
    path("4", views.uzumaki5, name="qswer"),
    path("5", views.uzumaki5, name="qswert")

    ,
]

