from django.contrib import admin
from .models import HomePageContent, AboutPageContent, Project, ContactDetail, ContactMessage, SkillCategory, Skill

# Register your models here.
@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    # Based on your current models.py, greeting and name fields are not present
    list_display = ('name',)

@admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    # Based on your current models.py, sub_heading and heading_span are not present
    list_display = ('initial_paragraph',)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1 # Number of empty forms to display

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'order',)
    inlines = [SkillInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_link', 'github_link', 'order',)
    list_editable = ('order',)

@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'url', 'order', 'icon_class',) # Added icon_class to list_display
    list_editable = ('url', 'order',) # Removed icon_class from list_editable as it's auto-filled
    readonly_fields = ('icon_class',) # Make icon_class read-only as it's auto-filled

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'email_subject', 'submitted_at',)
    readonly_fields = ('submitted_at',)