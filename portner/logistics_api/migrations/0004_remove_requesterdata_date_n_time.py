# Generated by Django 4.1.3 on 2022-11-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0003_requesterdata_riderdata_delete_addrequesterdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requesterdata',
            name='Date_n_Time',
        ),
    ]
