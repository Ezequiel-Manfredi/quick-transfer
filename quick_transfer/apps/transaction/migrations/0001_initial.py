# Generated by Django 5.1.2 on 2024-11-21 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('reason', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('emitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_sent', to='account.account')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reason.reason')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_received', to='account.account')),
            ],
        ),
    ]
