from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponse
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_GET, require_POST

from .models import *

# Create your views here.


@require_GET
def root(request):
    return redirect('/myapp')


@require_GET
def home(request):
    return render(request, 'home.html')


class LoginView(View):
    
    @method_decorator(require_GET)
    def get(self, request):
        return render(request, 'login.html')
    
    @method_decorator(require_POST)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        
        if user_auth is not None:
            login(request, user_auth)
            return redirect('notes_groups')
        else:
            return render(request, 'login.html', {
                'credentials_error': 'Credenciales erroneas'
            })
    
    
class RegisterView(View):
    
    @method_decorator(require_GET)
    def get(self, request):
        return render(request, 'register.html')
    
    @method_decorator(require_POST)
    def post(self, request):
        self._add_user(request)
        return render(request, 'login.html')
    
    @classmethod
    def _add_user(request):
        User.objects.create_user(
            username = request.POST['username'],
            first_name = request.POST['firstname'],
            last_name = request.POST['surname'],
            email = request.POST['email'],
            password = request.POST['password']
        ).save()
    

@require_GET
def close_session(request):
    logout(request)
    return redirect('home')
    

@require_GET
def notesGroups(request: HttpRequest):
    notesGroups = NotesGroup.objects.all()
    return render(request, 'notes_groups.html', {"notes_groups_list": notesGroups})


class NotesView(View):

    @method_decorator(login_required)
    @method_decorator(require_GET)
    def get(self, request, group_id):

        notesGroup = NotesGroup.objects.filter(id=group_id)[0]
        notes = Note.objects.filter(notes_group_id=group_id)

        return render(request, 'notes.html', {
            'notes_group': notesGroup,
            'notes_list': notes
        })
     
    
@login_required
@require_POST 
def updateNote(request: HttpRequest, note_id):
    note = Note.objects.get(pk=note_id)
    note.content = request.POST['card_content']
    note.save()
    return redirect(reverse('notes', args=(note.notes_group_id,)))