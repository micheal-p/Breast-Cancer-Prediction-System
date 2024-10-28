# Generated by Django 4.2.5 on 2024-10-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius_mean', models.FloatField()),
                ('prediction_result', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]