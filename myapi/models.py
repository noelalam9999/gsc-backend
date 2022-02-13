from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
        
class Students(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    gender = models.CharField(max_length=60) 
    birth_date = models.CharField(max_length=60)
    birth_month = models.CharField(max_length=60)
    birth_year = models.CharField(max_length=60)
    address1 = models.CharField(max_length=60, null=True, blank=True)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    prev_qualification = models.CharField(max_length=60)    
    IELTSBand = models.CharField(max_length=60, null=True, blank=True)  
    TOEFL = models.CharField(max_length=60, null=True, blank=True)    
    PTE = models.CharField(max_length=60, null=True, blank=True)    
    Duolingo = models.CharField(max_length=60, null=True, blank=True)    
    Desiredlevel = models.CharField(max_length=60, null=True, blank=True)    
    StudyDestination = models.CharField(max_length=60)    
    IntendedSemester = models.CharField(max_length=60, null=True, blank=True  )   
    DesiredSubject = models.CharField(max_length=60)    
    email = models.CharField(max_length=60, null=True, blank=True  )
    added_by = models.CharField(max_length=60, null=True, blank=True  )
    def __str__(self):
        return self.name
        
class Agents(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    agency_name = models.CharField(max_length=60)    
    
    mobile = models.CharField(max_length=60)
    website = models.CharField(max_length=60, null=True, blank=True)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    offices = models.CharField(max_length=60, null=True, blank=True)    
    subagents = models.CharField(max_length=60, null=True, blank=True)    
    YearFounded = models.CharField(max_length=60, null=True, blank=True)    
    number_of_staff = models.CharField(max_length=60, null=True, blank=True)    
    services_provided = models.CharField(max_length=60, null=True, blank=True) 
    charge = models.CharField(max_length=60, null=True, blank=True)
    students_sent_abroad = models.CharField(max_length=60, null=True, blank=True)    
    association_bin = models.CharField(max_length=60, null=True, blank=True)    
    associations = models.CharField(max_length=60, null=True, blank=True)    
    recruitment_area = models.CharField(max_length=60, null=True, blank=True)    
    facebooklink = models.CharField(max_length=60, null=True, blank=True) 
    email = models.CharField(max_length=60, null=True, blank=True  )
    added_by = models.CharField(max_length=60, null=True, blank=True  )
    active_status = models.CharField(max_length=60, null=True, blank=True  )
    def __str__(self):
        return self.name         

class TeamMember(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    email = models.CharField(max_length=60)  
    mobile = models.CharField(max_length=60)
    student_c = models.CharField(max_length=60, null=True, blank=True)
    student_r = models.CharField(max_length=60, null=True, blank=True)
    student_u = models.CharField(max_length=60, null=True, blank=True)    
    student_d = models.CharField(max_length=60, null=True, blank=True)    
    agent_c = models.CharField(max_length=60, null=True, blank=True)    
    agent_r = models.CharField(max_length=60, null=True, blank=True)    
    agent_u = models.CharField(max_length=60, null=True, blank=True) 
    agent_d = models.CharField(max_length=60, null=True, blank=True)
    service_provider_c = models.CharField(max_length=60, null=True, blank=True)    
    service_provider_r = models.CharField(max_length=60, null=True, blank=True)    
    service_provider_u = models.CharField(max_length=60, null=True, blank=True)    
    service_provider_d = models.CharField(max_length=60, null=True, blank=True)    
    institute_c = models.CharField(max_length=60, null=True, blank=True) 
    institute_r = models.CharField(max_length=60, null=True, blank=True)
    institute_u = models.CharField(max_length=60, null=True, blank=True)
    institute_d = models.CharField(max_length=60, null=True, blank=True)
    active_status = models.CharField(max_length=60, null=True, blank=True)
    def __str__(self):
        return self.name  

        
class Uni(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60)
    UGfee = models.CharField(max_length=60, null=True, blank=True)
    UGIELTSReq = models.CharField(max_length=60, null=True, blank=True)
    UGTOEFLReq = models.CharField(max_length=60, null=True, blank=True) 
    UGPTEReq = models.CharField(max_length=60, null=True, blank=True) 
    UGDuolingoReq = models.CharField(max_length=60, null=True, blank=True) 
    UGAppfee = models.CharField(max_length=60, null=True, blank=True) 
    UGExtra = models.CharField(max_length=60, null=True, blank=True)
    PGfee = models.CharField(max_length=60, null=True, blank=True)
    PGIELTSReq = models.CharField(max_length=60, null=True, blank=True)
    PGTOEFLReq = models.CharField(max_length=60, null=True, blank=True) 
    PGPTEReq = models.CharField(max_length=60, null=True, blank=True) 
    PGDuolingoReq = models.CharField(max_length=60, null=True, blank=True) 
    PGAppfee = models.CharField(max_length=60, null=True, blank=True)
    PGExtra = models.CharField(max_length=60, null=True, blank=True)
    Diplomafee = models.CharField(max_length=60, null=True, blank=True)
    AccomodationCostUG = models.CharField(max_length=60, null=True, blank=True)
    AccomodationCostPG = models.CharField(max_length=60, null=True, blank=True)
    FallSemester = models.CharField(max_length=60, null=True, blank=True)
    SpringSemester = models.CharField(max_length=60, null=True, blank=True)    
    SummerSemester = models.CharField(max_length=60, null=True, blank=True)
    Intake4 = models.CharField(max_length=60, null=True, blank=True)
    Intake5 = models.CharField(max_length=60, null=True, blank=True)    
    Intake6 = models.CharField(max_length=60, null=True, blank=True)
    FallSemesterAppDeadline = models.CharField(max_length=60, null=True, blank=True)
    SpringSemesterAppDeadline = models.CharField(max_length=60, null=True, blank=True)    
    SummerSemesterAppDeadline = models.CharField(max_length=60, null=True, blank=True)
    Intake4AppDeadline = models.CharField(max_length=60, null=True, blank=True)
    Intake5AppDeadline = models.CharField(max_length=60, null=True, blank=True)    
    Intake6AppDeadline = models.CharField(max_length=60, null=True, blank=True) 
    ranking = models.CharField(max_length=60, null=True, blank=True)    
    email = models.CharField(max_length=60, null=True, blank=True)
    HSCReqUG = models.CharField(max_length=60, null=True, blank=True)
    HSCReqPG = models.CharField(max_length=60, null=True, blank=True)
    UGReq = models.CharField(max_length=60, null=True, blank=True)
    MinDeposit = models.CharField(max_length=60, null=True, blank=True)
    Accomodation = models.CharField(max_length=60, null=True, blank=True)
    Internship = models.CharField(max_length=60, null=True, blank=True)
    OfferLetter = models.CharField(max_length=60, null=True, blank=True)
    WorkVisa = models.CharField(max_length=60, null=True, blank=True)
    WorkStudy = models.CharField(max_length=60, null=True, blank=True)
    ScholarshipReq = models.CharField(max_length=60, null=True, blank=True)
    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=60)
    partner = models.CharField(max_length=60)
    branches = models.CharField(max_length=60, null=True, blank=True)
    product_type = models.CharField(max_length=60)    
    approx_fee = models.CharField(max_length=60)
    revenue_type = models.CharField(max_length=60, null=True, blank=True)
    intake_month = models.CharField(max_length=60, null=True, blank=True)
    duration = models.CharField(max_length=60, null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name  


class Service(models.Model):
    name = models.CharField(max_length=60)
    partner = models.CharField(max_length=60)
    branches = models.CharField(max_length=60, null=True, blank=True)
    product_type = models.CharField(max_length=60)    
    approx_fee = models.CharField(max_length=60)
    revenue_type = models.CharField(max_length=60, null=True, blank=True)

    duration = models.CharField(max_length=60, null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name         
        

class Application(models.Model):
    client_name = models.CharField(max_length=60)
    applied_intake_date = models.CharField(max_length=60, null=True, blank=True)
    client_phone = models.CharField(max_length=60, null=True, blank=True)
    client_assignee = models.CharField(max_length=60, null=True, blank=True)    
    application_assignee = models.CharField(max_length=60, null=True, blank=True)
    product = models.CharField(max_length=60, null=True, blank=True)
    partner = models.CharField(max_length=60, null=True, blank=True)
    partner_branches = models.CharField(max_length=60, null=True, blank=True)
    partners_client_id = models.CharField(max_length=60, null=True, blank=True)
    work_flow = models.CharField(max_length=60, null=True, blank=True)
    application_start_by = models.CharField(max_length=60, null=True, blank=True)
    application_start_by_branch = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=60, null=True, blank=True)
    stage_in_queue = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.CharField(max_length=60, null=True, blank=True)
    def __str__(self):
        return self.client_name

class Program(models.Model):
    program_name = models.CharField(max_length=60)
    duration = models.CharField(max_length=60, null=True, blank=True)
    required_ielts = models.CharField(max_length=60, null=True, blank=True)
    fee = models.CharField(max_length=60, null=True, blank=True)    
    department = models.CharField(max_length=60, null=True, blank=True)
    partner = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name        
        
class User(models.Model):
    email = models.CharField(max_length=60)
    usertype = models.CharField(max_length=60)
      
    
    def __str__(self):
        return self.email   
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.title 
        
class IELTSCert(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email

class LatestDegree(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email

class AgentCert(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email   

class UniLogo(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class UserProfilePicture(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email         
# Create your models here.
