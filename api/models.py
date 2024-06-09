from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    
    date = models.DateField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class Technology(models.Model):
    FRONTEND = 'frontend'
    BACKEND = 'backend'
    
    CATEGORY_CHOICES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='technology_images/')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('CEO', 'Co-Founder & CEO'),
        ('CTO', 'CTO'),
        ('Developer', 'Developer'),
        ('Intern', 'Intern'),
        ('Trainee', 'Trainee'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    applicant_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cvs/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job_title}"

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title