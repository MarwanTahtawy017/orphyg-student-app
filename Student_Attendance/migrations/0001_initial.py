# Generated by Django 2.2.3 on 2019-09-25 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student_Info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Attended', models.BooleanField(default=False)),
                ('Student_Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_Info.GroupsList')),
                ('This_Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student_Info.Student')),
            ],
        ),
    ]
