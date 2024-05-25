"""
URL configuration for projet_attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin_app.views import *
from student_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('login/',login_view,name='login'),
<<<<<<< HEAD

=======
>>>>>>> 5da2088a835957f8855f20ff368f10a06f7d0a1a
    path('administration/Gérer_Enseignant',administration,name="Gérer_Enseignant"),
    path('administration/Gérer_Etudiant',Gérer_Etudiant,name="Gérer_Etudiant"),
    path('administration/Gérer_Modele',Gérer_Modele,name="Gérer_Modele"),
    path('administration/AjouterEnseignant',AjouterEnseignant,name="AjouterEnseignant"),
    path('administration/AjouterEtudiant',AjouterEtudiant,name="ajouterEtudiant"),
    # path('seanceDeCours/',seanceDeCours,name='seanceDeCours'),
    path('seanceDeCours/',seanceDeCours,name='seanceDeCours'),
    path('enseignant/' , enseignant , name='enseignant'),
    path('ListeCours/' , listeCours , name='listeCours'),
    path('AjouterCours/' , ajouterCours , name='ajouterCours'),
    path('ModifierCours/' , modifierCours , name='modifierCours'),
    path('remarque/' , remarque , name='remarque'),
<<<<<<< HEAD

=======
    path('ListeEtudiants/' , ListeEtudiants , name='ListeEtudiants')
>>>>>>> 5da2088a835957f8855f20ff368f10a06f7d0a1a
    # path(page_teacher,page_teacher,name='page_teacher'),
]
