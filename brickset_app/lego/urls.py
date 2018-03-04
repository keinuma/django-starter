
# url()関数、include関数のインポート
from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [

    # ex /lego/
    path('',  views.index, name='lego_index'),

    # ex /lego/1/edit
    path('<int:lego_id>/edit/', views.edit, name='lego_edit'),

    # ex /lego/1/delete
    path('<int:lego_id>/delete/', views.delete, name='lego_delete'),

    # ほしい物リストへの追加
    # ex /lego/1/add/wish_list/
    path('<int:lego_id>/add/wish_list/', views.add_to_wish_list, name='lego_add_wish_list'),

    # ほしい物リストから削除
    # ex /lego/1/delete/wish_list/
    path('<int:lego_id>/delete/wish_list/', views.delete_from_wish_list, name='lego_delete_wish_list'),

    # ほしい物リストの一覧
    # ex /lego/wish_list/
    path('wish_list/', views.wish_list_index, name='wish_list_index')

]
