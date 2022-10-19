from django.urls import path
from mysangpum import views


urlpatterns = [   
    
    path('list', views.ListFunc), 
    path('insert', views.InsertFunc),
    path('insertok', views.InsertOkFunc),
    path('update', views.UpdateFunc),
    path('updateok', views.UpdateOkFunc),
    path('delete', views.DeleteFunc), 
     
]