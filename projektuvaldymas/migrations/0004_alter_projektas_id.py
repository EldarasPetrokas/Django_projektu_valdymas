# Generated by Django 5.1.4 on 2024-12-18 13:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projektuvaldymas", "0003_alter_darbuotojas_id_alter_projektas_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projektas",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
