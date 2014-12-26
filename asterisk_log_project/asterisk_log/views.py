from datetime import timedelta
from django.db.models.query_utils import Q
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
    if not request.user.is_superuser:
        phone = request.user.username
        calls = calls.filter(Q(src=phone) | Q(dst=phone))

    if form.is_valid():
        if form.cleaned_data['phone']:
            calls = calls.filter(Q(src=form.cleaned_data['phone']) | Q(dst=form.cleaned_data['phone']))
        if form.cleaned_data['date']:
            calls = calls.filter(calldate__range=[form.cleaned_data['date'], form.cleaned_data['date'] + timedelta(days=1)])
        if form.cleaned_data['date_start']:
            calls = calls.filter(calldate__gte=form.cleaned_data['date_start'])
        if form.cleaned_data['date_end']:
            calls = calls.filter(calldate__lte=form.cleaned_data['date_end'] + timedelta(days=1))
        if form.cleaned_data['duration_from']:
            calls = calls.filter(duration__gte=form.cleaned_data['duration_from'])
        if form.cleaned_data['duration_to']:
            calls = calls.filter(duration__lte=form.cleaned_data['duration_to'])
        if form.cleaned_data['source']:
            calls = calls.filter(src=form.cleaned_data['source'])
        if form.cleaned_data['destination']:
            calls = calls.filter(dst=form.cleaned_data['destination'])
    return {'form': form, 'calls': calls.select_related()}
