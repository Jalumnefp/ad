from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('groups/', NotesGroupsView.as_view(), name='notes_groups'),
    path('group/<int:group_id>', NotesView.as_view(), name="notes")
]