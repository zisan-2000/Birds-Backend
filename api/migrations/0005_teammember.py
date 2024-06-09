# Generated by Django 5.0.4 on 2024-06-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_technology_delete_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('CEO', 'Co-Founder & CEO'), ('CTO', 'CTO'), ('Developer', 'Developer')], max_length=50)),
                ('image', models.ImageField(upload_to='team_images/')),
            ],
        ),
    ]
