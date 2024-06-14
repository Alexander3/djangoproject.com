# Generated by Django 3.2.25 on 2024-05-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0005_feeditem_add_index_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='localdjangocommunity',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('D', 'Denied'), ('A', 'Approved')], default='P', max_length=1),
        ),
    ]