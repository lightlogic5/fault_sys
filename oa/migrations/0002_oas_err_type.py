# Generated by Django 2.0.5 on 2018-07-12 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oas',
            name='err_type',
            field=models.CharField(choices=[('oa', '电子公文'), ('ht', '合同系统'), ('mes', 'MES')], default=1, max_length=3, verbose_name='故障类别'),
        ),
    ]
