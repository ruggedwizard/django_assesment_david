# Generated by Django 5.0.1 on 2024-02-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_expense_category_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('TRANSPORT', 'TRANSPORT'), ('FOOD', 'FOOD'), ('DATA', 'DATA'), ('SAVINGS', 'SAVINGS'), ('MISCELLANEOUS', 'MISCELLANEOUS')], default='MISCELLANEOUS', error_messages={'invalid_choice': 'Invalid value. Choose from {BUDGET_TYPES}'}, max_length=255),
        ),
    ]
