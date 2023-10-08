"""
URL configuration for inklings_prototype project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import include, path

from app import views

urlpatterns = [
    path('', views.MemoListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', next_page='home'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('memo/<int:pk>/', views.MemoListView.as_view(), name='view_memo'),
    path('memos/new/', views.MemoCreateAndRedirectToEditView.as_view(), name='new_memo'),
    path('memo/<int:pk>/edit/', views.MemoEditView.as_view(), name='edit_memo'),
    path('memo/<int:pk>/delete/', views.DeleteMemoView.as_view(), name='delete_memo'),

    path('tag/<int:pk>/', views.TagFeedView.as_view(), name='view_tag'),
    path('tag/<int:pk>/delete/', views.DeleteTagView.as_view(), name='delete_tag'),
    path('tag/<int:pk>/edit/', views.UpdateTagView.as_view(), name='update_tag'),
    path('tags/merge/', views.merge_tags, name='merge_tags'),
    
    path('inkling/<int:pk>/', views.InklingFeedView.as_view(), name='view_inkling'),
    path('inkling/<int:pk>/delete/', views.DeleteInklingView.as_view(), name='delete_inkling'),
    path('inklings/create/', views.CreateInklingView.as_view(), name='create_inkling'),
    
    path('search/', views.QueryFeedView.as_view(), name='search'),
    
    path('links/create/', views.CreateLinkView.as_view(), name='create_link'),
    path('link/<int:pk>/delete/', views.DeleteLinkView.as_view(), name='delete_link'),
    
    path('link_types/', views.LinkTypeListView.as_view(), name='link_types'),
    path('link_types/create', views.CreateLinkTypeView.as_view(), name='create_link_type'),
    path('link_type/<int:pk>/edit/', views.EditLinkTypeView.as_view(), name='edit_link_type'),
    path('link_type/<int:pk>/delete/', views.DeleteLinkTypeView.as_view(), name='delete_link_type'),
    
    path('martor/', include('martor.urls')),
]
