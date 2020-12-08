"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from personal.views import (
	home_screen_view,
    about_view,
    contact_view,
    contact_success,
    resume_view,
    photo_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    myadmin_logout_view,
    account_view,
    must_authenticate_view,
    denied_view,
    login_as_different_user,
)




urlpatterns = [
	path('', home_screen_view, name="home"),
	path('about/', about_view, name="about"),
	path('contact/', contact_view, name="contact"),
    path('resume/', resume_view, name="resume"),
    path('image/<slug>', photo_view, name="image"),
    path('contact_success/', contact_success, name="contact_success"),
    path('projects/', include('projects.urls', 'projects')),	    
    path('admin/', admin.site.urls),

    #account
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('change_user/', login_as_different_user, name="change_user"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, name="register"),
    path('access_denied/', denied_view, name="access_denied"),
    path('account/', account_view, name="account"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    

    # #rest framework
    # path('api/blog/', include('blog.api.urls', 'blog_api')),

    # #myadmin
    path('myadmin/', include('myadmin.urls', 'myadmin')),
    path('admin_logout/', myadmin_logout_view, name="myadmin_logout"),


    #others

    path('captcha/', include('captcha.urls')),
    # re_path(r'^tinymce/', include('tinymce.urls')),
    
    # path('', views.main, name='main'),url(r'^pdf', views.pdf, name='pdf'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


