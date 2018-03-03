"""brickset_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# url()関数、include関数のインポート
from django.conf.urls import include, url
from django.contrib import admin
# from django.urls import path

urlpatterns = [

    # itemアプリケーションのURL設定を追加
    url(r'^item/', include('item.urls')),

    # 管理サイト
    url('^admin/', admin.site.urls),
]
