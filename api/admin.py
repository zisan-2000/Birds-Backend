from django.contrib import admin
from .models import Blog, Technology, TeamMember, ContactForm, JobApplication, JobPost

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'image')
    search_fields = ('title', 'author')
    list_filter = ('date',)
    ordering = ('-date',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'image')
    search_fields = ('name', 'role')
    list_filter = ('role',)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job_title', 'cv', 'cover_letter', 'additional_info')
    search_fields = ('applicant_name', 'job_title')

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'location')
    search_fields = ('title', 'location')