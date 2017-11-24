from django.shortcuts import render
from django.http import HttpResponse
from .myutils.response import make_response

import json


# Create your views here.
def chat(request):
    if request.method == 'POST' and request.is_ajax():
        query = request.POST.get('query', None)
        response = make_response(query)

        return HttpResponse(json.dumps({'response': response}), content_type="application/json")

    else:
        return render(request, 'chat_with_dog_master/chatting.html', {})


