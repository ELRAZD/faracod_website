from django.shortcuts import render, redirect
from django.contrib import messages

from .models import SiteSettings, IntroMessage, HeroSection, AboutSection, ContentBlock
from services.models import Feature
from projects.models import Project
from contact.forms import ContactForm, ProjectRequestForm


def home(request):
    contact_form = ContactForm()
    project_form = ProjectRequestForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type', 'contact')
        if form_type == 'project':
            project_form = ProjectRequestForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                messages.success(
                    request,
                    'درخواست پروژه شما ثبت شد. به زودی با شما تماس می‌گیریم.'
                )
                return redirect('/#home')
        else:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'پیام شما با موفقیت ارسال شد.')
                return redirect('/#conect')

    features = Feature.objects.all()
    context = {
        'intro': IntroMessage.load(),
        'hero': HeroSection.load(),
        'about': AboutSection.load(),
        'content_block': ContentBlock.load(),
        'activities': features.filter(group=Feature.GROUP_ACTIVITY),
        'about_features': features.filter(group=Feature.GROUP_ABOUT),
        'introduce_features': features.filter(group=Feature.GROUP_INTRODUCE),
        'options': features.filter(group=Feature.GROUP_OPTION),
        'content_items': features.filter(group=Feature.GROUP_CONTENT),
        'projects': Project.objects.filter(is_active=True),
        'contact_form': contact_form,
        'project_form': project_form,
    }
    return render(request, 'home.html', context)