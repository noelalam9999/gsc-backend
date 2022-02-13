from django.contrib import admin
from .models import Hero
from .models import Students
from .models import Agents
from .models import Uni
from .models import Post
from .models import User
from .models import Product
from .models import Service
from .models import LatestDegree
from .models import TeamMember
from .models import IELTSCert
from .models import AgentCert
from .models import Application
from .models import UniLogo
from .models import UserProfilePicture


admin.site.register(Hero)
admin.site.register(Students)
admin.site.register(Agents)
admin.site.register(Uni)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(LatestDegree)
admin.site.register(IELTSCert)
admin.site.register(AgentCert)
admin.site.register(Application)
admin.site.register(UniLogo)
admin.site.register(UserProfilePicture)
admin.site.register(TeamMember)