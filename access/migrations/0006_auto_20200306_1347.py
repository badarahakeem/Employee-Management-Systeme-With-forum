# Generated by Django 2.0 on 2020-03-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0005_auto_20200303_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DG', 'DG'), ('COO', 'COO'), ('COE', 'COE'), ('DRH', 'DRH'), ('Manager', 'Manager'), ('Developper', 'Developper'), ('Commercial(e)', 'Commercial(e)'), ('Autres', 'Autres')], max_length=20),
        ),
    ]
