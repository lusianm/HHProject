# Generated by Django 3.0 on 2020-05-26 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userWeb', '0004_auto_20200522_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='exerciseList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userWeb.ExerciseList'),
        ),
    ]
