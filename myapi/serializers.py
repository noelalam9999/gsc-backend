from rest_framework import serializers

from .models import Hero
from .models import Students
from .models import Agents
from .models import Uni
from .models import Post
from .models import User
from .models import Product
from .models import Service
from .models import LatestDegree
from .models import IELTSCert
from .models import AgentCert
from .models import Application
from .models import UniLogo
from .models import Program
from .models import UserProfilePicture
from .models import PassportPicture
from .models import SSCCert
from .models import HSCCert
from .models import BachelorCert
from .models import SSCTranscript
from .models import HSCTranscript
from .models import BachelorTranscript
from .models import BachelorMarksheet
from .models import Lor1
from .models import Lor2
from .models import Lor3
from .models import Sop
from .models import CV
from .models import BankSolvency
from .models import TeamMember
from .models import NewsletterCampaign
from .models import ContactForm

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name', 'partner','branches','product_type','approx_fee','revenue_type','duration','description')

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id','client_name', 'applied_intake_date','client_phone','client_assignee','application_assignee','product','partner','partner_branches','partners_client_id','work_flow','application_start_by','application_start_by_branch','status','stage_in_queue','created_at')
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'partner','branches','product_type','approx_fee','revenue_type','intake_month','duration','description')
        
class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ('id','email','HSCGPA','UGCGPA','added_by','name','mobile','country','gender','birth_date','birth_month','birth_year','address1','address2','prev_qualification','IELTSBand','TOEFL','PTE','Duolingo','Desiredlevel','StudyDestination','IntendedSemester','DesiredSubject','work_experience','prev_institution','parents_name','parents_contact_number','parents_email','parents_profession','extracurricular','created_at','updated_at' )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','usertype')        
        
class AgentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agents
        fields = ('id','name','email','role','agency_name','country','mobile','website','offices','subagents','YearFounded','number_of_staff','services_provided','students_sent_abroad','association_bin','associations','recruitment_area','charge','added_by','active_status','created_at','updated_at')
        
class UniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uni
        fields = ('id','name','mobile','email','country','MinDeposit','UGfee','PGfee','Diplomafee','AccomodationCostUG','AccomodationCostPG','FallSemester','SpringSemester','SummerSemester','Intake4','Intake5','Intake6','FallSemesterAppDeadline','SpringSemesterAppDeadline','SummerSemesterAppDeadline','Intake4AppDeadline','Intake5AppDeadline','Intake6AppDeadline','ranking', 'HSCReqUG','HSCReqPG','Accomodation','Internship','OfferLetter','WorkVisa','WorkStudy','UGIELTSReq','UGTOEFLReq','UGPTEReq','UGDuolingoReq','UGAppfee','PGIELTSReq','PGTOEFLReq','PGPTEReq','PGDuolingoReq','PGAppfee','ScholarshipReq','UGExtra','PGExtra','UGReq')

class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ('id','program_name','duration','required_ielts','fee','department','partner' )

class NewsletterCampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsletterCampaign
        fields = ('id','campaign_name','recipient_list','message','subj' )

class ContactFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactForm
        fields = ('id','name','recipient','message' )

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id','name','role','email','mobile','student_c','student_r','student_u','student_d','agent_c','agent_r','agent_u','agent_d','service_provider_c','service_provider_r','service_provider_u','service_provider_d','institute_c','institute_r','institute_u','institute_d','active_status' )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LatestDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestDegree
        fields = '__all__'

class IELTSCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = IELTSCert
        fields = '__all__' 

class AgentCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentCert
        fields = '__all__'

class UniLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniLogo
        fields = '__all__'

class UserProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfilePicture
        fields = '__all__'

class PassportPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportPicture
        fields = '__all__'

class SSCCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCCert
        fields = '__all__'

class HSCCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSCCert
        fields = '__all__'

class BachelorCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BachelorCert
        fields = '__all__'

class SSCTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCTranscript
        fields = '__all__'

class HSCTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSCTranscript
        fields = '__all__'

class BachelorTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BachelorTranscript
        fields = '__all__'

class BachelorMarksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BachelorMarksheet
        fields = '__all__' 

class Lor1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lor1
        fields = '__all__'

class Lor2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lor2
        fields = '__all__'

class Lor3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lor3
        fields = '__all__'

class SopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sop
        fields = '__all__'

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'

class BankSolvencySerializer(serializers.ModelSerializer):
    class Meta:
        model = BankSolvency
        fields = '__all__'

        