# Generated by Django 4.0.1 on 2022-01-21 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_customuser_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='strategy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.strategy'),
        ),
    ] 
