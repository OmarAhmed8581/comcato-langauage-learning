# Generated by Django 4.2.10 on 2024-03-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_favouritetopic_interest_material_userdetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.CharField(choices=[('free', 'Free Download'), ('premium', 'Premium')], default='free', max_length=20),
        ),
    ]
