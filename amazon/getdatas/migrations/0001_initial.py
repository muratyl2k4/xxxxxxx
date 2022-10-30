# Generated by Django 4.1.1 on 2022-10-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Veriler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("SIRA_NO", models.IntegerField()),
                ("TARIH", models.DateField()),
                ("ASIN", models.CharField(max_length=100)),
                ("ALICI_SIPARIS_NUMARASI", models.CharField(max_length=100)),
                ("SATICI_SIPARIS_NUMARASI", models.CharField(max_length=100)),
                ("SATIS_FIYATI", models.FloatField()),
                ("AMAZON_FEE", models.FloatField()),
                ("KAR", models.FloatField()),
                ("YUZDELIK_KAR", models.FloatField()),
            ],
        ),
    ]