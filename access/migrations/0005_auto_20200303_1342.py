# Generated by Django 3.0.2 on 2020-03-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_auto_20200303_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('1', 'DG'), ('2', 'COO'), ('3', 'COE'), ('4', 'DRH'), ('5', 'Manager'), ('6', 'Developper'), ('7', 'Commercial(e)'), ('8', 'Autres')], max_length=20),
        ),
    ]
