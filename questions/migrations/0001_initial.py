# Generated by Django 2.0.4 on 2018-04-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
            ],
        ),
    ]
