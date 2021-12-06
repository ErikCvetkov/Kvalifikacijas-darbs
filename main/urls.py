from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from account.views import (
    registration_view,
    docAppl_view
)

urlpatterns = [
    path('', views.index, name='home'),
    path('register', registration_view, name='register'),
    path('docAppl', docAppl_view, name='docAppl'),
    path('thankYouPage', views.thankYouPage, name='thankYouPage'),
    path('logout', views.logoutUser, name='logout'),
    path('user', views.User, name='user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

