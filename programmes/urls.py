from django.urls import path
from programmes.views import *
app_name = "programmes"
urlpatterns = [

    path('', NiveauListView.as_view(), name = "niveaulist"),
    path('<slug:slug>', MatiereListView.as_view(), name = "matierelist"),
    path('<str:niveau>/<slug:slug>/', LeconListView.as_view(), name = "leconlist"),
    path('<str:niveau>/<str:slug>/create/', LeconCreateView.as_view(), name = "leconcreate"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/', LeconListViewDetail.as_view(), name = "leconlistdetail"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/update', LeconUpdateView.as_view(), name = "leconupdate"),
    path('<str:niveau>/<str:matiere>/<slug:slug>/delete', LeconDeleteView.as_view(), name = "lecondelete"),
    
    
]