# Generated by Django 4.1.7 on 2023-04-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_txt', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
