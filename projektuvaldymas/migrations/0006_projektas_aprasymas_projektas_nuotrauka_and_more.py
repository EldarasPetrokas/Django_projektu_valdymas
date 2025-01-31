# Generated by Django 5.1.4 on 2024-12-19 11:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projektuvaldymas", "0005_alter_saskaita_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="projektas",
            name="aprasymas",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="projektas",
            name="nuotrauka",
            field=models.ImageField(
                blank=True, null=True, upload_to="projekto_nuotraukos/"
            ),
        ),
        migrations.AlterField(
            model_name="projektas",
            name="darbai",
            field=models.ManyToManyField(
                related_name="projektai", to="projektuvaldymas.darbas"
            ),
        ),
        migrations.AlterField(
            model_name="projektas",
            name="darbuotojai",
            field=models.ManyToManyField(
                related_name="projektai", to="projektuvaldymas.darbuotojas"
            ),
        ),
        migrations.AlterField(
            model_name="projektas",
            name="klientas",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projektai",
                to="projektuvaldymas.klientas",
            ),
        ),
        migrations.AlterField(
            model_name="projektas",
            name="saskaitos",
            field=models.ManyToManyField(
                related_name="projektai", to="projektuvaldymas.saskaita"
            ),
        ),
        migrations.AlterField(
            model_name="projektas",
            name="vadovas",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vadovaujami_projektai",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
