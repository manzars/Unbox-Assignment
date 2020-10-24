from django.shortcuts import render
from django.http import JsonResponse
from developers.models import Developer
from common.models import *
from user.models import User
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.exceptions import NotFound

from .serializers import DeveloperSerializer, DeveloperCreateSerializer, UserSerializer
from .offerLetter import create_offer_letter

# Create your views here.


@api_view(["GET"])
def error_page(request):
    return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def apiOverview(request):
    data = {"error": "not a valid endpoint", "create user": "/api/create-user/",
            "developer list": ["/api/developer", ["GET", "POST"]], "developer detail": ["/api/developer-detail", ["GET", "PUT", "DELETE"]]}
    return Response(data)


def get_object_dict(result):
    result['designation'] = Designation.objects.get(
        id=result['designation']).name
    result['employment_type'] = EmploymentType.objects.get(
        id=result['employment_type']).name

    tech_stack_result = []
    for value in result['tech_stack']:
        tech_stack_result.append(TechStack.objects.get(
            id=value).name)

    result['tech_stack'] = tech_stack_result

    user_result = model_to_dict(
        User.objects.get(id=result['user']))

    user_result.pop('id')

    result['user'] = user_result

    return result


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        usr_data = request.data
        new_usr = User.objects.create(
            name=usr_data['name'], age=usr_data['age'], sex=usr_data['sex'], email=usr_data['email'])
        new_usr.save()
        serializer = UserSerializer(new_usr)
        return Response(serializer.data)


class DeveloperList(APIView):
    serializer_class = DeveloperCreateSerializer

    def get(self, request, format=None):
        developer = Developer.objects.all()
        serializer = DeveloperSerializer(developer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeveloperCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = get_object_dict(serializer.data)
            create_offer_letter(result['user']['name'], result['location'],
                                result['designation'], result['start_date'], result['annual_ctc'])
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeveloperDetail(APIView):
    serializer_class = DeveloperCreateSerializer

    def get_object(self, pk):
        try:
            return Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        developer = self.get_object(pk)
        serializer = DeveloperSerializer(developer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        developer = self.get_object(pk)
        serializer = DeveloperCreateSerializer(developer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = get_object_dict(serializer.data)
            print(result['user']['name'])
            create_offer_letter(result['user']['name'], result['location'],
                                result['designation'], result['start_date'], result['annual_ctc'])
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        developer = self.get_object(pk)
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
