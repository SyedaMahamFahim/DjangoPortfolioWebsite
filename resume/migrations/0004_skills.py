# Generated by Django 3.1.7 on 2021-07-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210703_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=150)),
                ('section_description', models.CharField(max_length=255)),
                ('skill_one', models.CharField(max_length=150)),
                ('skill_two', models.CharField(max_length=150)),
                ('skill_three', models.CharField(max_length=150)),
                ('skill_four', models.CharField(max_length=150)),
                ('skill_five', models.CharField(max_length=150)),
                ('skill_six', models.CharField(max_length=150)),
            ],
        ),
    ]
