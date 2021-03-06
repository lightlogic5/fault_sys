# Generated by Django 2.0.5 on 2018-07-16 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0003_auto_20180716_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errsys',
            name='err_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='errsys_e', to='oa.ErrSysType', verbose_name='故障类别'),
        ),
        migrations.AlterField(
            model_name='errsystype',
            name='type_name',
            field=models.CharField(max_length=15, verbose_name='故障类别'),
        ),
    ]
