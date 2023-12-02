from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', close_session, name='logout'),
    path('groups/', notesGroups, name='notes_groups'),
    path('group/<int:group_id>', NotesView.as_view(), name='notes'),
    path('notes/<int:note_id>/update', updateNote, name='note_update'),
]