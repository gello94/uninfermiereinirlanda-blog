from django.urls import path
from .views import get_experiences, get_experience_details, add_or_edit_experience

urlpatterns = [
    path('', get_experiences, name='get_experiences'),
    path('<int:id>/', get_experience_details, name='get_experience_details'),
    path('aggiungi_esperienza/', add_or_edit_experience, name="add_experience"),
    path('<int:pk>/modifica_esperienza/',
         add_or_edit_experience, name="edit_experience"),

]
