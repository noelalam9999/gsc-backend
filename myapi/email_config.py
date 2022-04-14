from django.core.mail import send_mail
from django.conf import settings
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template,render_to_string
from django.template import Context
from django.utils.html import strip_tags

def Convert(string):
    li = list(string.split(" "))
    return li

def send_a_mail(subject, message, recipient_list,name):
    plaintext = get_template('welcome_text_student.txt')
    htmly = get_template('welcome_email_student.html')
    d = { 'name': name }
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_new_student(subject, message, recipient_list,name,mobile):
    
    htmly = render_to_string('new_student.html',{ 'name': name,'mobile':mobile })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_welcome_agent(subject, message, recipient_list,name):
    htmly = render_to_string('welcome_email_agent.html',{ 'name': name })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_set_pw(subject, message, recipient_list,name):
    htmly = render_to_string('agent_set_pw.html',{ 'name': name })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_new_agent(subject, message, recipient_list,name,mobile):
    htmly = render_to_string('new_agent.html',{ 'name': name,'mobile':mobile })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')
    
def send_a_mail_new_staff(subject, message, recipient_list,name,email):
    htmly = render_to_string('welcome_moderator.html',{ 'name': name,'email':email })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')
    
def send_a_mail_new_application(subject, message, recipient_list,name,partner):
    htmly = render_to_string('application_start.html',{ 'name': name,'partner':partner })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_updated_application(subject, message, recipient_list,name,partner,status):
    htmly = render_to_string('application_updated.html',{ 'name': name,'partner':partner,'status':status })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')
    
def send_a_mail_newsletter(subject, message, recipients):
    htmly = message
    plain_message = "plain message"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = recipients.split()
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipient_list)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')

def send_a_mail_contact_form_client(subject, message, recipients,name):
    htmly = render_to_string('contact_form.html',{ 'name': name })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipients)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent') 

def send_a_mail_contact_form_admin(subject, message, recipients,name,email):
    htmly = render_to_string('contact_form_admin.html',{ 'name': name,'message':message,'email':email })
    plain_message = strip_tags(htmly)
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, plain_message, email_from, recipients)
    msg.attach_alternative(htmly, "text/html")
    msg.send()
    #send_mail(subject, message, email_from, recipient_list )
    print('email sent')    


    