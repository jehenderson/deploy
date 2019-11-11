from django.http import HttpResponse, JsonResponse
from django.core import serializers
import urllib.request, json, platform

def send_to_API(url, data):
  req = urllib.request.Request(url, data=data, method='POST',
                                 headers={'Content-Type': 'application/json'})
  urllib.request.urlopen(req, data)

class LoggingMiddleware(object):
    """docstring for ."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        url = "https://npky8rle0m.execute-api.us-east-1.amazonaws.com/default/analytics"
        # if request.method == 'GET':
        #     req = urllib.request.Request(url)
        # elif request.method == 'POST':
        #     data = request.body
        #     req = urllib.request.Request(url, data)
        # else:
        #     return("Bad request type")
        # response = urllib.request.urlopen(req)

        data = {
            "pathname": request.path,
            "language": request.META['HTTP_ACCEPT_LANGUAGE'],
            "platform": "platform.platform",
            "userAgent": request.META['HTTP_USER_AGENT'],
            "location": {
            "latitude": 0,
            "longitude": 0
            }
        }
        send_to_API(url, json.dumps(data).encode('utf8'))
