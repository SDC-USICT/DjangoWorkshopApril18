# Generated by Django 2.0.4 on 2018-04-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
