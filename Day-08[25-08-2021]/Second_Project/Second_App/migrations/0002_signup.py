# Generated by Django 3.0 on 2021-08-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Second_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
