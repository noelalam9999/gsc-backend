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
router.register(r'newsletter-campaign', views.NewsletterCampaignViewSet)
router.register(r'contact-form', views.ContactFormViewSet)
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
    path('profilepicture/', views.UserProfilePictureView.as_view(), name= 'profilepicture_list'),
    path('passportpicture/', views.PassportPictureView.as_view(), name= 'passportpicture_list'),
    path('ssccert/', views.SSCCertView.as_view(), name= 'ssccert_list'),
    path('hsccert/', views.HSCCertView.as_view(), name= 'hsccert_list'),
    path('bachelorcert/', views.BachelorCertView.as_view(), name= 'bachelorcert_list'),
    path('ssctranscript/', views.SSCTranscriptView.as_view(), name= 'ssctranscript_list'),
    path('hsctranscript/', views.HSCTranscriptView.as_view(), name= 'hsctranscript_list'),
    path('bachelortranscript/', views.BachelorTranscriptView.as_view(), name= 'bachelortranscript_list'),
    path('bachelormarksheet/', views.BachelorMarksheetView.as_view(), name= 'bachelormarksheet_list'),
    path('lor1/', views.Lor1View.as_view(), name= 'lor1_list'),
    path('lor2/', views.Lor2View.as_view(), name= 'lor2_list'),
    path('lor3/', views.Lor3View.as_view(), name= 'lor3_list'),
    path('sop/', views.SopView.as_view(), name= 'sop_list'),
    path('cv/', views.CVView.as_view(), name= 'cv_list'),
    path('banksolvency/', views.BankSolvencyView.as_view(), name= 'banksolvency_list')
    
    # path('admin/', admin.site.urls),
    # path('api/', include('post.urls')),
]