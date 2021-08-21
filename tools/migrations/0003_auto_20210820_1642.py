# Generated by Django 3.2.6 on 2021-08-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_rename_kanrezec_intgroove'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntTurning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('dmin', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('ap', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('W', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('Wp', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('Lmax', models.DecimalField(decimal_places=1, max_digits=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='RastRezec',
        ),
    ]
