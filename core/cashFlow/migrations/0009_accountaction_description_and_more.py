# Generated by Django 4.1.3 on 2023-03-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cashFlow", "0008_accountaction_created_at_accountaction_updated_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountaction",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Açıklama"),
        ),
        migrations.AlterField(
            model_name="accountaction",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi"),
        ),
        migrations.AlterField(
            model_name="accountaction",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi"),
        ),
    ]