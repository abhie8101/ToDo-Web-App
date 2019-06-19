from django.urls import path
from todos import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('todos/',views.todo),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('signin/',views.sign_in),
    path('homepage/',views.homepage),
    path('logout/',views.log_out,name = "logout"),
    path('delete/(?P<todoid>\w{0,50})/$',views.delete, name='delete'),

]
