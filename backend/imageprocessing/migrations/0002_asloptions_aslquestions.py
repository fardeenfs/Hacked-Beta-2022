# Generated by Django 4.0.4 on 2022-11-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageprocessing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASLOptions',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option_text', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ASLQuestions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('difficulty', models.TextField()),
                ('color', models.TextField()),
                ('option1', models.IntegerField(default=None)),
                ('option2', models.IntegerField(default=None)),
                ('option3', models.IntegerField(default=None)),
                ('option4', models.IntegerField(default=None)),
                ('correct_option', models.IntegerField()),
            ],
        ),
    ]
