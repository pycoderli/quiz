# Generated by Django 2.0 on 2017-12-28 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brainstorm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='level',
            fields=[
                ('levelnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('ans', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='levelentry',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='current_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='brainstorm.level'),
        ),
    ]
