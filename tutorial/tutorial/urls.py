from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from polls import views


router = DefaultRouter()
router.register('questions', views.QuestionViewSet)

app_name = 'polls'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

    path('api/auth/', obtain_jwt_token),
    path('api/', include(router.urls)),
    path('api/choices/<int:choice_id>/vote/', views.VoteView.as_view()),
]
