# Generated by Django 4.1.6 on 2023-02-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountName', models.CharField(blank=True, max_length=250, null=True, verbose_name='Hesap Adı')),
                ('accountAmount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Toplam Tutar')),
            ],
            options={
                'verbose_name': 'Hesap Adı',
                'verbose_name_plural': 'Hesaplar',
            },
        ),
    ]