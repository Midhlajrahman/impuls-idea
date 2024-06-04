# Generated by Django 5.0.6 on 2024-06-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_alter_product_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="service",
            options={"ordering": ("order",), "verbose_name_plural": "Service"},
        ),
        migrations.AddField(
            model_name="service",
            name="order",
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
