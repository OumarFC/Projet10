"""
URL configuration for SoftDesk project.

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
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from Project.views import ProjectViewSet
from Issue.views import IssueViewSet
from User.views import ContributorViewSet, UserViewSet
from Comment.views import CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_nested import routers


router = SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
users_router = routers.NestedSimpleRouter(router, r'projects', lookup='user')

projects_router.register(r'issues', IssueViewSet, basename='issues')
projects_router.register(r'users', ContributorViewSet)

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(users_router.urls)),
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup')
]
