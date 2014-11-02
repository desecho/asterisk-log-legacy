from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from annoying.decorators import render_to
from .forms import CallForm
from .models import Call


def logout_view(request):
    logout(request)
    return redirect('/login/')


@render_to('index.html')
@login_required
def home(request):
    form = CallForm(request.POST or None)
    calls = Call.objects.all()
    if form.is_valid():
        if form.cleaned_data['date_start']:
            calls = calls.filter(calldate__gte=form.cleaned_data['date_start'])
        if form.cleaned_data['date_end']:
            calls = calls.filter(calldate__lte=form.cleaned_data['date_end'])
        if form.cleaned_data['duration_from']:
            calls = calls.filter(duration__gte=form.cleaned_data['duration_from'])
        if form.cleaned_data['duration_to']:
            calls = calls.filter(duration__lte=form.cleaned_data['duration_to'])
        if form.cleaned_data['source']:
            calls = calls.filter(src=form.cleaned_data['source'])
        if form.cleaned_data['destination']:
            calls = calls.filter(dst=form.cleaned_data['destination'])

    return {'form': form, 'calls': calls}
