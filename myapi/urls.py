from django.urls import include, path
from rest_framework import routers
from . import views

from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'students', views.StudentsViewSet)
router.register(r'agents', views.AgentsViewSet)
router.register(r'uni', views.UniViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'application', views.ApplicationViewSet)
router.register(r'program', views.ProgramViewSet)
router.register(r'team-member', views.TeamMemberViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', views.PostView.as_view(), name= 'posts_list'),
    path('latestdegree/', views.LatestDegreeView.as_view(), name= 'latestdegree_list'),
    path('ieltscert/', views.IELTSCertView.as_view(), name= 'ieltscert_list'),
    path('agentcert/', views.AgentCertView.as_view(), name= 'agentcert_list'),
    path('unilogo/', views.UniLogoView.as_view(), name= 'unilogo_list'),
    path('profilepicture/', views.UserProfilePictureView.as_view(), name= 'profilepicture_list')
    # path('admin/', admin.site.urls),
    # path('api/', include('post.urls')),
]