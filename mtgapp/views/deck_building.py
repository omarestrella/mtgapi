from django import http
from django.views import generic


class SSETestView(generic.View):
    def get(self, request, *args, **kwargs):
        response = http.HttpResponse(mimetype='text/event-stream')
        response.content = 'data: Message\n\n'

        return response
