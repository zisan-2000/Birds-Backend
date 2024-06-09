from django.urls import path
from . import views

from .views import (
    BlogList, BlogCreate, BlogDetail,
    TechnologyList, TechnologyCreate, TechnologyDetail,
    TeamMemberList, TeamMemberCreate, TeamMemberDetail,
    ContactFormList, ContactFormCreate, ContactFormDetail,
    JobApplicationList, JobApplicationCreate, JobApplicationDetail, JobPostList, JobPostCreate, JobPostDetail
)

urlpatterns = [
    path('Bloglist/', views.BlogList.as_view(), name='blog-list'),
    path('Blogcreate/', views.BlogCreate.as_view(), name='blog-create'),
    path('Blogdetail/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    
    path('technologylist/', views.TechnologyList.as_view(), name='technology-list'),
    path('technologycreate/', views.TechnologyCreate.as_view(), name='technology-create'),
    path('technologydetail/<int:pk>/', views.TechnologyDetail.as_view(), name='technology-detail'),
    
    path('team-member-list/', views.TeamMemberList.as_view(), name='team-member-list'),
    path('team-member-create/', views.TeamMemberCreate.as_view(), name='team-member-create'),
    path('team-member-detail/<int:pk>/', views.TeamMemberDetail.as_view(), name='team-member-detail'),

    path('contact-form/', ContactFormList.as_view(), name='contact-form-list'),
    path('contact-form/create/', ContactFormCreate.as_view(), name='contact-form-create'),
    path('contact-form/<int:pk>/', ContactFormDetail.as_view(), name='contact-form-detail'),

    # New views for Job Application
    path('job-application-list/', JobApplicationList.as_view(), name='job-application-list'),
    path('job-application-create/', JobApplicationCreate.as_view(), name='job-application-create'),
    path('job-application-detail/<int:pk>/', JobApplicationDetail.as_view(), name='job-application-detail'),

    # New views for Job Posts
    path('job-post-list/', JobPostList.as_view(), name='job-post-list'),
    path('job-post-create/', JobPostCreate.as_view(), name='job-post-create'),
    path('job-post-detail/<int:pk>/', JobPostDetail.as_view(), name='job-post-detail'),
]
