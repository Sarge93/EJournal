# Generated by Django 2.0.3 on 2018-03-20 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Journal')),
            ],
        ),
    ]
