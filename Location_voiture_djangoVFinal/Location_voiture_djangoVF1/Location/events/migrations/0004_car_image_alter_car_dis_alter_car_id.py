# Generated by Django 4.1.7 on 2023-04-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_car_dis'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=' ', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='dis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
