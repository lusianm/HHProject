# Generated by Django 3.0 on 2020-05-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userWeb', '0006_auto_20200526_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='Age10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='Age20',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='Age30',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='Age40',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='BMIH',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='BMIL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='BMIN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='BMIO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='SexM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='SexY',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Part1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Part2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Part3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Part4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='BMI',
            field=models.CharField(choices=[('남성', 'Man'), ('여성', 'Woman')], default='정상', max_length=20),
        ),
    ]
