# Generated by Django 4.1.2 on 2022-11-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookSwiping", "0024_alter_genre_nyt_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdemographics",
            name="birth_date",
            field=models.DateField(default=None, null=True),
        ),
    ]