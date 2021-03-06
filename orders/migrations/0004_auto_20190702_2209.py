# Generated by Django 2.0.3 on 2019-07-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_custom_user_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='orders',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='content',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
