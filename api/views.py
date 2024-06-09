from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import BlogSerializer, TechnologySerializer, TeamMemberSerializer, ContactFormSerializer, JobApplicationSerializer, JobPostSerializer
from .models import Blog, Technology, TeamMember, ContactForm, JobApplication, JobPost




class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCreate(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class TechnologyList(ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyCreate(CreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TeamMemberList(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberCreate(CreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberDetail(RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class ContactFormList(ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class ContactFormCreate(CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class ContactFormDetail(RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class JobApplicationList(ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationCreate(CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationDetail(RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobPostList(ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostCreate(CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostDetail(RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer