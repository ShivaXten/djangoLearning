from django.shortcuts import redirect

class RedirectToRegisterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('/users/dashboard/'):
            return redirect('register')
        return self.get_response(request)