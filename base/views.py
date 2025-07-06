from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages # Import messages for feedback
from .models import HomePageContent, AboutPageContent, Project, ContactDetail, ContactMessage, SkillCategory

def test(request):
    home_content = HomePageContent.objects.first()
    about_content = AboutPageContent.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    contact_details = ContactDetail.objects.all()

    # Create dummy instances if no content exists (for initial setup)
    if not home_content:
        home_content = HomePageContent.objects.create()
    if not about_content:
        about_content = AboutPageContent.objects.create()

    context = {
        'home_content': home_content,
        'about_content': about_content,
        'skill_categories': skill_categories,
        'projects': projects,
        'contact_details': contact_details,
    }
    return render(request, 'index.html', context)

def contact_form_submit(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        mobile_number = request.POST.get('mobile_number')
        email_subject = request.POST.get('email_subject')
        message = request.POST.get('message')

        if full_name and email_address and message:
            ContactMessage.objects.create(
                full_name=full_name,
                email_address=email_address,
                mobile_number=mobile_number,
                email_subject=email_subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all required fields (Full Name, Email Address, and Your Message).')