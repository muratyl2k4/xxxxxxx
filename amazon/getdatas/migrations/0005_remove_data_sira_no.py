# Generated by Django 4.1.1 on 2022-10-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("getdatas", "0004_alter_data_alici_siparis_numarasi_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="data", name="SIRA_NO",),
    ]
