# Generated by Django 3.0.4 on 2020-04-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Imagen'),
        ),
    ]