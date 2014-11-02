from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from annoying.decorators import ajax_request, render_to

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('/login/')


@render_to('index.html')
@login_required
def home(request):
    return {}
