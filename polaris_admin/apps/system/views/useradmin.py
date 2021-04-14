from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Userinfo(APIView):
    def post(self,request):
        return Response(data={"post method"},status=status.HTTP_200_OK)
