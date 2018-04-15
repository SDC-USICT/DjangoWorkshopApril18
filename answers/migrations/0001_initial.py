# Generated by Django 2.0.4 on 2018-04-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('upvote', models.IntegerField()),
                ('downvote', models.IntegerField()),
                ('question_id', models.ForeignKey(on_delete='CASCADE', to='questions.Question')),
            ],
        ),
    ]
