# Generated by Django 3.1.7 on 2021-07-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20210703_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='testimonials_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
