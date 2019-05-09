# Generated by Django 2.2 on 2019-05-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190509_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('cardiologist', 'cardiologist'), ('ophthalmologist', 'ophthalmologist'), ('neuropathologist', 'neuropathologist'), ('surgeon', 'surgeon'), ('otorhinolaryngologist', 'otorhinolaryngologist'), ('endocrinologist', 'endocrinologist')], default='endocrinologist', max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(choices=[('I10-Arterial hypertension', 'I10-Arterial hypertension'), ('J42-Chronical bronchitis', 'J42-Chronical bronchitis'), ('J06.9- cold', 'J06.9- cold'), ('M42-osteochondrosis', 'M42-osteochondrosis'), ('E10- diabetes', 'E10- diabetes'), ('Z04.8-others', 'Z04.8-others')], default='Z04.8-others', max_length=100),
        ),
    ]
