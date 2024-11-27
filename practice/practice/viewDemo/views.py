from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import User
import json


class Index(View):

    def get(self, request) -> HttpResponse:
        users = User.objects.all()
        serliazed = [{"name": user.name} for user in users]
        return HttpResponse(json.dumps(serliazed))
      
    def post(self, request) -> HttpResponse:
        data = json.loads(request.body)
        user = User(name=data['name'], age=data['age'], email=data['email'])
        user.save()
        return HttpResponse(json.dumps(f"{user.id}, {user.name} is saved"))


def update_user(request, id: int) -> HttpResponse:
    user = User.objects.get(id=id)
    data = json.loads(request.body)
    user.name = data['name']
    user.email = data['email']
    user.save()
    return HttpResponse(json.dumps(f"{user.name} and {user.email}"))

