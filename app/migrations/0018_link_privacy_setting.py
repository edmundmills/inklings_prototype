# Generated by Django 4.2.5 on 2023-10-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_inkling_privacy_setting_memo_privacy_setting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='privacy_setting',
            field=models.CharField(choices=[('private', 'Private'), ('friends', 'Friends'), ('friends_of_friends', 'Friends of Friends')], default='private', max_length=20),
        ),
    ]
