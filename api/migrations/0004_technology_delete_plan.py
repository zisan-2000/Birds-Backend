# Generated by Django 5.0.4 on 2024-06-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend')], max_length=10)),
                ('image', models.ImageField(upload_to='technology_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]