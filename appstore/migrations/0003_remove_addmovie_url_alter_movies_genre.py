# Generated by Django 4.0.6 on 2022-08-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_rename_user_customers_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmovie',
            name='url',
        ),
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY')], max_length=10),
        ),
    ]
