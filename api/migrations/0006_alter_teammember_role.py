# Generated by Django 5.0.4 on 2024-06-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_teammember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.CharField(choices=[('CEO', 'Co-Founder & CEO'), ('CTO', 'CTO'), ('Developer', 'Developer'), ('Intern', 'Intern'), ('Trainee', 'Trainee')], max_length=50),
        ),
    ]
