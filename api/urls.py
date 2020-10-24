from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = views.error_page

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('create-user/', views.UserAPIView.as_view(), name='user-create'),
    path('developer/', views.DeveloperList.as_view(), name='dev-check'),
    path('developer-detail/<str:pk>',
         views.DeveloperDetail.as_view(), name='dev-detail'),
]
