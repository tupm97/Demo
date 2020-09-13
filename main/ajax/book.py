import json
from main.decorator import ajax_required
from django.views import View
from django.http import HttpResponse
from django.urls import resolve
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from main.models import Book

class BookAjaxView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        self.context = {"data": []}
        self.request_body = {}
        self.request_url_name = None
        self.response = HttpResponse(json.dumps(self.context), "application/json")

    @csrf_exempt
    # @method_decorator(ajax_required)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.request_url_name = resolve(request.path).url_name
        self.request_body = json.loads(request.body.decode('utf-8')) if self.request.body else None
        return super(BookAjaxView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        books = Book.objects.all()
        result = dict()
        book_arr = []
        for book in books:
            book_arr.append(model_to_dict(book))
        result['data'] = book_arr
        self.context['data'] = result
        self.response.content = json.dumps(self.context)
        return self.response

    def post(self, request):
        pass