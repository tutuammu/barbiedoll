
from django.urls import path
from . import views
app_name='barbieapp'
urlpatterns = [
    path('',views.copying,name='copying'),
    path('cutie/<int:barb_id>/',views.detail,name='detail'),
    path('adding/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('deleted/<int:id>/',views.deleted,name='deleted')
]