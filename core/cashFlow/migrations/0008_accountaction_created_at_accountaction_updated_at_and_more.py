# Generated by Django 4.1.7 on 2023-03-02 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashFlow', '0007_remove_accountaction_customertitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-03-02 00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='accountaction',
            name='CustomerTitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashFlow.customer', verbose_name='Firma Adı'),
        ),
        migrations.AlterField(
            model_name='accountaction',
            name='accountName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashFlow.accountbox', verbose_name='Hesap Adı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CustomerTitle',
            field=models.CharField(default='Firma Seçiniz', max_length=255, verbose_name='Firma Ünvanı'),
        ),
    ]