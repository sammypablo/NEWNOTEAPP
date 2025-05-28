from .views import main, user_notes, detail, create, login_view, register_view, logout_view
from django.urls import path
from .views import edit
from .views import delete
urlpatterns = [
    path('', login_view, name='default'),
    path('home', user_notes, name="user-note"),
    path('note/<int:id>', detail, name="detail-page"),
    path('create', create, name="create-note"),
    path('signin', login_view, name="login"),
    path('signup', register_view, name="signup"),
    path('logout', logout_view, name="logout"),
    path('edit/<int:id>/', edit, name="edit"),       
    path('delete/<int:id>/', delete, name="delete")

]