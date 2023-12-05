from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', close_session, name='logout'),
    path('groups/', notesGroups, name='notes_groups'),
    path('group/<int:user_id>/create', createGroup, name='notes_groups_create'),
    path('group/<int:group_id>/update', updateGroup, name='notes_groups_update'),
    path('group/<int:group_id>/delete', deleteGroup, name='notes_groups_delete'),
    path('group/<int:group_id>', notes, name='notes'),
    path('notes/<int:group_id>/create', createNote, name='note_create'),
    path('notes/<int:note_id>/update', updateNote, name='note_update'),
    path('notes/<int:note_id>/delete', deleteNote, name='note_delete'),
]