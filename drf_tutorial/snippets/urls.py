from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('snippets/', views.SnippetListGeneric.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetailGeneric.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
