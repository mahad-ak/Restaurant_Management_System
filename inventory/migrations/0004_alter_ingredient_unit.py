# Generated by Django 3.2.4 on 2021-06-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('tbsp', 'Tablespoon'), ('lbs', 'Pounds'), ('oz', 'Ounces'), ('unit', 'Unit'), ('g', 'Grams')], default='unit', max_length=200),
        ),
    ]
