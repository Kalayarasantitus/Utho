# Generated by Django 5.1.3 on 2024-11-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utho_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='files/')),
                ('file_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]