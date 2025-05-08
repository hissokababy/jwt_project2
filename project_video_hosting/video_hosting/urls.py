from django.urls import path

from video_hosting.views import LoadVideoView, MyVideoView

urlpatterns = [
    path('api/v1/load_video/', LoadVideoView.as_view()),
    path('api/v1/video/<int:pk>/', MyVideoView.as_view()),

]
