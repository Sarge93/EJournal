from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from journal.forms import *


def index(request) :
    return HttpResponse("Hello world!!!")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'test.html', {'form': form})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/journal/login"
    template_name = "register2.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login2.html"
    success_url = "/journal/main"
    def form_valid(self,form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
