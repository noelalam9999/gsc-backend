from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

from .serializers import StudentsSerializer
from .models import Students

from .serializers import AgentsSerializer
from .models import Agents

from .serializers import UniSerializer
from .models import Uni

from .serializers import UserSerializer
from .models import User

from .serializers import PostSerializer
from .models import Post

from .serializers import IELTSCertSerializer
from .models import IELTSCert

from .serializers import LatestDegreeSerializer
from .models import LatestDegree

from .serializers import AgentCertSerializer
from .models import AgentCert

from .serializers import ProductSerializer
from .models import Product

from .serializers import ServiceSerializer
from .models import Service

from .serializers import ApplicationSerializer
from .models import Application

from .serializers import ProgramSerializer
from .models import Program

from .serializers import UniLogoSerializer
from .models import UniLogo

from .serializers import UserProfilePictureSerializer
from .models import UserProfilePicture

from .serializers import TeamMemberSerializer
from .models import TeamMember


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('name')
    serializer_class = StudentsSerializer
    
class AgentsViewSet(viewsets.ModelViewSet):
    queryset = Agents.objects.all().order_by('name')
    serializer_class = AgentsSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer        
    
class UniViewSet(viewsets.ModelViewSet):
    queryset = Uni.objects.all().order_by('name')
    serializer_class = UniSerializer    

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('client_name')
    serializer_class = ApplicationSerializer    

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all().order_by('program_name')
    serializer_class = ProgramSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all().order_by('name')
    serializer_class = TeamMemberSerializer    

    
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UniLogoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = UniLogo.objects.all()
        serializer = UniLogoSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = UniLogoSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class IELTSCertView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = IELTSCert.objects.all()
        serializer = IELTSCertSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = IELTSCertSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LatestDegreeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = LatestDegree.objects.all()
        serializer = LatestDegreeSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = LatestDegreeSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgentCertView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = AgentCert.objects.all()
        serializer = AgentCertSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = AgentCertSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

class UserProfilePictureView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = UserProfilePicture.objects.all()
        serializer = UserProfilePictureSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = UserProfilePictureSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                  

            
# Create your views here.
