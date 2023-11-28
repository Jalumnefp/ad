from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import HttpRequest
from .models import *

# Create your views here.


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    

class NotesGroupsView(View):

    def get(self, request):

        notesGroups = NotesGroup.objects.all()

        return render(request, 'notes_groups.html', {"notes_groups_list": notesGroups})
    

class NotesView(View):

    def get(self, request, group_id):

        notesGroup = NotesGroup.objects.filter(id=group_id)[0]
        notes = Note.objects.filter(notes_group_id=group_id)

        return render(request, 'notes.html', {
            'notes_group': notesGroup,
            'notes_list': notes
        })
        
    def post(self, request: HttpRequest, group_id):
        print(group_id, request)
        print(request.POST.items)
        return render(request, 'notes.html')