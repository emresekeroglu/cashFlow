# Generated by Django 4.1.3 on 2023-02-17 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashFlow', '0006_rename_customers_accountaction_customertitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountaction',
            name='CustomerTitle',
        ),
        migrations.RemoveField(
            model_name='accountaction',
            name='accountName',
        ),
        migrations.AlterField(
            model_name='accountbox',
            name='accountName',
            field=models.CharField(blank=True, default='empty value', max_length=250, null=True, verbose_name='Hesap Adı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CustomerTitle',
            field=models.CharField(default='empty value', max_length=255, verbose_name='Firma Ünvanı'),
        ),
        migrations.AddField(
            model_name='accountaction',
            name='CustomerTitle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cashFlow.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountaction',
            name='accountName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cashFlow.accountbox'),
            preserve_default=False,
        ),
    ]
