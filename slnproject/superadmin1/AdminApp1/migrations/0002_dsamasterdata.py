# Generated by Django 5.0.7 on 2024-11-01 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DSAMasterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MasterDataImage', models.ImageField(upload_to='DSA/MasterData/')),
            ],
        ),
    ]