from django.contrib.auth import views
from django.urls import path
from django.conf.urls import url
from . import views
# from accounts import views
# from mysite.startmyproject import views as core_views

urlpatterns = [
    # path('signup/',views.signup,name='signup'),
     url(r'^$',views.home),
     url(r'^signupst',views.signupst),
     url(r'^signupmen',views.signupmen),
     url(r'^about',views.aboutus),
     url(r'^homein',views.homein),
     url(r'^homein',views.mentor),
    # path('signup/', , name='signup'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #  path('signup/', views.SignUp.as_view(), name='signup'),
    #  url(r'^signup/$', core_views.signup, name='signup'),
]