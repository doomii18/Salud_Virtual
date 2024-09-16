# Generated by Django 4.2.16 on 2024-09-12 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientCode', models.CharField(max_length=6)),
                ('Birthdate', models.DateField()),
                ('Allergies', models.TextField(max_length=200, null=True)),
                ('Active', models.BooleanField()),
                ('IdPerson', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Person.person')),
            ],
            options={
                'db_table': 'Patients',
            },
        ),
    ]
