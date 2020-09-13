from django.http import HttpResponseBadRequest

def ajax_required(func):
    def func_wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
    return func_wrapper