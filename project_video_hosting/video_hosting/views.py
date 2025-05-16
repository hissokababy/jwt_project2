import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from video_hosting.serializers import LoadVideoSerializer
from video_hosting.services.user import VideoHostingService
# Create your views here.


class LoadVideoView(APIView):
    permission_classes = [AllowAny]
    service = VideoHostingService()

    def post(self, request):
        serializer = LoadVideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = self.service.create_video(user=request.user, 
                                          title=serializer.validated_data.get('title'),
                                          preview=serializer.validated_data.get('preview'), 
                                          video=serializer.validated_data.get('video'),
                                          duration=serializer.validated_data.get('duration'))

        self.service.process_video(input_file=video.video, resolutions=[240, 720], file_name='hls_video',
                                   video_id=video.pk)

        return Response(status=status.HTTP_202_ACCEPTED)
    

class MyVideoView(APIView):
    permission_classes = [AllowAny]
    service = VideoHostingService()

    def get(self, request, pk):
        video = self.service.get_video(user_id=request.user.pk, video_id=pk)

        return Response(video, status=status.HTTP_202_ACCEPTED)
    
