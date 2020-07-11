from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render, redirect, render_to_response

User = get_user_model()
@login_required(login_url='/log_in/')
def user_list(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'app/user_list.html', {'users': users})
# Create your views here.
data = [['100',10],['90',9],['80',8]]
def graph(request):
    return render(request,'app/graph.html',{
                                            'data': data,
                                            },
                                            )

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('app:user_list'))
        else:
            print(form.errors)
    return render(request, 'app/log_in.html', {'form': form})

@login_required(login_url='/log_in/')
def log_out(request):
    logout(request)
    return redirect(reverse('app:log_in'))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app:log_in'))
        else:
            print(form.errors)
    return render(request, 'app/sign_up.html', {'form': form})