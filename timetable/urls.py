from . import views
from django.urls import path, include

urlpatterns=  [
    path('', views.index, name='index'),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('accounts/',views.index,name="index"),
    path('post',views.post,name="post"),
    path('tablecreationpage', views.tableCreationPage, name="create-table"),
    ]