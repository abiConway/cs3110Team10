# Generated by Django 4.2 on 2024-05-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan_app', '0002_remove_mealplan_profile_profile_meal_plan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='ingredient_amount',
            field=models.TextField(null=True),
        ),
    ]
