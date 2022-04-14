from django.db import models
from .email_config import send_a_mail,send_a_mail_new_student,send_a_mail_welcome_agent,send_a_mail_new_agent,send_a_mail_new_staff,send_a_mail_new_application,send_a_mail_updated_application,send_a_mail_newsletter,send_a_mail_contact_form_client,send_a_mail_contact_form_admin, send_a_mail_set_pw
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver



class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
        
class Students(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60, null=True, blank=True)
    mobile = models.CharField(max_length=60)
    country = models.CharField(max_length=60, null=True, blank=True)
    gender = models.CharField(max_length=60, null=True, blank=True) 
    birth_date = models.CharField(max_length=60, null=True, blank=True)
    birth_month = models.CharField(max_length=60, null=True, blank=True)
    birth_year = models.CharField(max_length=60, null=True, blank=True)
    address1 = models.CharField(max_length=60, null=True, blank=True)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    HSCGPA = models.CharField(max_length=60, null=True, blank=True)
    UGCGPA = models.CharField(max_length=60, null=True, blank=True)
    prev_qualification = models.CharField(max_length=60, null=True, blank=True)    
    IELTSBand = models.CharField(max_length=60, null=True, blank=True)  
    TOEFL = models.CharField(max_length=60, null=True, blank=True)    
    PTE = models.CharField(max_length=60, null=True, blank=True)
    Duolingo = models.CharField(max_length=60, null=True, blank=True)    
    Desiredlevel = models.CharField(max_length=60, null=True, blank=True)    
    StudyDestination = models.CharField(max_length=60, null=True, blank=True)    
    IntendedSemester = models.CharField(max_length=60, null=True, blank=True)   
    DesiredSubject = models.CharField(max_length=60, null=True, blank=True) 
    work_experience = models.CharField(max_length=60, null=True, blank=True)
    prev_institution = models.CharField(max_length=60, null=True, blank=True)
    parents_name = models.CharField(max_length=60, null=True, blank=True)
    parents_contact_number = models.CharField(max_length=60, null=True, blank=True)
    parents_email = models.CharField(max_length=60, null=True, blank=True)
    parents_profession = models.CharField(max_length=60, null=True, blank=True)
    extracurricular = models.CharField(max_length=60, null=True, blank=True)
    
    added_by = models.CharField(max_length=60, null=True, blank=True  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        
        if self.pk is None : 
            subj = f'Welcome {self.name}'
            message = f'Hello {self.name}, Welcome to GSC!'
            recipient_list = [self.email, ]
            send_a_mail(subj, message, recipient_list,self.name)
            subj2 = f'New Student {self.name}'
            message2 = f'A new student has just registered into GSC. Name : {self.name}'
            #recipient_list2 = ["noel.alam9999@gmail.com" ]    
            recipient_list2 = ["d_bdc.contacts@yahoo.com","contactsintbd@yahoo.com","contactsintbd@gmail.com","noel.alam9999@gmail.com" ]
            send_a_mail_new_student(subj2, message2, recipient_list2,self.name,self.mobile)
            super(Students, self).save(*args, **kwargs)
            
        else: 
            super(Students, self).save(*args, **kwargs)
    
        
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
    email = models.CharField(max_length=60, null=True, blank=True)
    added_by = models.CharField(max_length=60, null=True, blank=True)
    active_status = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        
        if self.pk is None :
            if self.added_by=="gsc":
                subj = f'Welcome {self.name}'
                message = f'Hello {self.name}, Welcome to GSC!'
                recipient_list = [self.email, ]
                send_a_mail_set_pw(subj, message, recipient_list,self.name) 
                
            else:
                subj = f'Welcome {self.name}'
                message = f'Hello {self.name}, Welcome to GSC!'
                recipient_list = [self.email, ]
                send_a_mail_welcome_agent(subj, message, recipient_list,self.name)
                subj2 = f'New Agent {self.name}'
                message2 = f'A new agent has just registered into GSC. Name : {self.name}'
                #recipient_list2 = ["noel.alam9999@gmail.com" ]
                recipient_list2 = ["d_bdc.contacts@yahoo.com","noel.alam9999@gmail.com" ]
                send_a_mail_new_agent(subj2, message2, recipient_list2,self.name,self.mobile)
                super(Agents, self).save(*args, **kwargs)
                
        else: 
            
            super(Agents, self).save(*args, **kwargs)
    
    
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
    
    def save(self, *args, **kwargs):
        
        if self.pk is None : 
            subj = f'Welcome {self.name}'
            message = f'Hello {self.name}, Welcome to GSC!'
            recipient_list = [self.email, ]
            send_a_mail_new_staff(subj, message, recipient_list,self.name,self.email)
            super(TeamMember, self).save(*args, **kwargs)
        else: 
            
            super(TeamMember, self).save(*args, **kwargs)
    
    
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
    
    
    def save(self, *args, **kwargs):
        uni = Uni.objects.get(id=self.partner)
        if self.pk is None : 
            subj = f'New Application by {self.client_name}'
            message = f'Hello {self.client_name}, Welcome to GSC!'
            recipient_list = ["d_bdc.contacts@yahoo.com" ]
            send_a_mail_new_application(subj, message, recipient_list,self.client_name,uni)
            super(Application, self).save(*args, **kwargs)
        else: 
            subj = f'Update on {uni} application'
            message = f'Hello {self.client_name}, Welcome to GSC!'
            recipient_list = [self.client_name ]
            send_a_mail_updated_application(subj, message, recipient_list,self.client_name,uni,self.status)
            super(Application, self).save(*args, **kwargs)
    
    
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
        
class NewsletterCampaign(models.Model):
    campaign_name = models.CharField(max_length=60)
    recipient_list = models.CharField(max_length=60, null=True, blank=True)
    message = models.CharField(max_length=30000, null=True, blank=True)
    subj = models.CharField(max_length=60, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        
        if self.pk is None :
            send_a_mail_newsletter(self.subj, self.message, self.recipient_list)
            super(NewsletterCampaign, self).save(*args, **kwargs)
        else: 
            
            super(NewsletterCampaign, self).save(*args, **kwargs)

    def __str__(self):
        return self.campaign_name

class ContactForm(models.Model):
    name = models.CharField(max_length=60)
    recipient = models.CharField(max_length=60, null=True, blank=True)
    message = models.CharField(max_length=30000, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        subj_client = "Thank you for reaching-out"
        subj_admin = "Contact form entry"
        moderator_mail = ["d_bdc.contacts@yahoo.com"]
        recipient_list = [self.recipient, ]
        send_a_mail_contact_form_client(subj_client, self.message, recipient_list,self.name)
        send_a_mail_contact_form_admin(subj_admin, self.message, moderator_mail,self.name,self.recipient)
        super(ContactForm, self).save(*args, **kwargs)
        

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
        
class PassportPicture(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class SSCCert(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class HSCCert(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class BachelorCert(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class SSCTranscript(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class HSCTranscript(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class BachelorTranscript(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class BachelorMarksheet(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class Lor1(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class Lor2(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class Lor3(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class Sop(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class CV(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email 

class BankSolvency(models.Model):
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    
    def __str__(self):
        return self.email         
# Create your models here.
