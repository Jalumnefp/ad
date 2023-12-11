from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_GET, require_POST

from .models import *

# Create your views here.

# ROOT
@require_GET
def root(request):
    return redirect('/myapp')
# END ROOT

# HOME
@require_GET
def home(request):
    return render(request, 'home.html')
# END HOME

# LOGIN
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
    def _add_user(self, request):
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

# END LOGIN 
    

# NOTE_GROUPS
@login_required
@require_GET
def notesGroups(request: HttpRequest):
    notesGroups = NotesGroup.objects.all()
    return render(request, 'notes_groups.html', {"notes_groups_list": notesGroups})

@login_required
@require_POST
def createGroup(request: HttpRequest, user_id):
    NotesGroup.objects.create(title=request.POST['title'], description=request.POST['description'], user_id=user_id).save()
    return redirect('notes_groups')

@login_required
@require_POST
def updateGroup(request: HttpRequest, group_id):
    group = NotesGroup.objects.get(pk=group_id)
    group.title = request.POST['title']
    group.description = request.POST['description']
    group.save()
    return redirect('notes_groups')

@login_required
@require_POST
def deleteGroup(request: HttpRequest, group_id):
    group = get_object_or_404(NotesGroup, pk=group_id)
    group.delete()
    return redirect('notes_groups')
# END NOTE_GROUPS


# NOTES    
@login_required
@require_GET
def notes(request, group_id):
    notesGroup = get_list_or_404(NotesGroup, id=group_id)[0]
    notes = Note.objects.filter(notes_group_id=group_id)

    return render(request, 'notes.html', {
        'notes_group': notesGroup,
        'notes_list': notes
    })
    
@login_required
@require_GET
def favouriteNotes(request: HttpRequest, user_id):
    notes = get_list_or_404(Note, favourite=True, notes_group_id__user_id=user_id)
    return render(request, 'static_notes.html', {'notes': notes})
    

@login_required
@require_POST
def createNote(request: HttpRequest, group_id):
    Note.objects.create(title='Write title', content='Write content', notes_group_id=group_id).save()
    return redirect(reverse('notes', args=(group_id,)))
  
@login_required
@require_POST 
def updateNoteTitle(request: HttpRequest, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.title = request.POST['title']
    note.save()
    return redirect(reverse('notes', args=(note.notes_group_id,)))

@login_required
@require_POST 
def updateNoteDescription(request: HttpRequest, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.content = request.POST['description']
    note.save()
    return redirect(reverse('notes', args=(note.notes_group_id,)))

@login_required
@require_POST
def updateNoteFavourite(request: HttpRequest, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.favourite = request.POST['favourite']
    note.save()
    return redirect(reverse('notes', args=(note.notes_group_id,)))


@login_required
@require_POST
def deleteNote(request: HttpRequest, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note_id = note.notes_group_id
    note.delete()
    return redirect(reverse('notes', args=(note_id,)))


# END NOTES