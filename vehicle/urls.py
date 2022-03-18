from django.urls import path,include
from vehicle import views 

urlpatterns = [
    path('<str:names>/',views.vehicle_form,name='vehicle_insert'),
    path('update/<str:na>/<int:id>/',views.vehicle_form,name='vehicle_update'),
    path('delete/<str:name>/<int:id>/',views.vehicle_delete,name='vehicle_delete'),
    path('list/<str:name>/',views.vehicle_list,name='vehicle_list')
]
